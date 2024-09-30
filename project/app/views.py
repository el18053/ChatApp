from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.views import View
from app.models import Room

# Create your views here.

class index(View):

    def get(self, request):
        """
        view to get all the Users from the db
        """
        if not request.user.is_authenticated:
            return redirect("login-user")

        # Exclude the logged-in user and superusers
        users = User.objects.filter(is_superuser=False).exclude(id=request.user.id)

        context = {
            'users' : users
        }
        return render(request, 'index.html', context)

    def post(self, request):
        # Get all users
        users = User.objects.filter(is_superuser=False)

        """
        view to connect sender and receiver in a chat room
        """
        sender = request.user.id
        receiver = request.POST['users']
        
        sender_user = User.objects.get(id=sender)
        receiver_user = User.objects.get(id=receiver)

        print("sender : {}".format(sender_user))
        print("receiver : {}".format(receiver_user))
        #sending the receiver as a session variable
        request.session['receiver_user'] = receiver

        #check if there is already a room betweem sender and receiver

        get_room = Room.objects.filter(Q(sender_user=sender_user, receiver_user=receiver_user) | Q(sender_user=receiver_user, receiver_user=sender_user))
        
        #if the room already exists return it
        if get_room :
            room_name = get_room[0].room_name

        #else create a new room
        else :
            new_room = "_".join(sorted([str(sender_user), str(receiver_user)]))

            """
            while True:
                room_exists = Room.objects.filter(room_name=new_room)
                if room_exists:
                    new_room = "_".join(sorted([str(sender_user), str(receiver_user)]))
                else :
                    break
            """
            create_room = Room.objects.create(sender_user=sender_user, receiver_user=receiver_user, room_name=new_room)

            create_room.save()
            room_name = create_room.room_name
            print("room_name : {}".format(room_name))

        return redirect('chat-page', roomName=room_name)

class chatPage(View):
    def get(self, request, roomName, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login-user")
        
        get_object_or_404(Room, room_name=self.kwargs.get("roomName"))
        room = Room.objects.get(room_name=self.kwargs.get("roomName"))

        context = {
            "roomName" : str(room)
        }
        return render(request, "chatPage.html", context)