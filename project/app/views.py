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
        return render(request, 'index_2.html', context)

    def post(self, request):
        """
        view to connect sender and receiver in a chat room
        """
        sender = request.user.id
        receivers = request.POST.getlist('users')

        print("receiver : {}".format(receivers))
        
        sender_user = User.objects.get(id=sender)
        receiver_users = [User.objects.get(id=receiver) for receiver in receivers]

        print("sender_user : {}".format(sender_user))
        print("receiver_user : {}".format(receiver_users))
        #sending the receiver as a session variable
        #request.session['receiver_user'] = receiver

        #check if there is already a room betweem sender and receiver
        #get_room = Room.objects.filter(Q(sender_user=sender_user, receiver_user=receiver_user) | Q(sender_user=receiver_user, receiver_user=sender_user))
        users = [sender_user]
        users = users + receiver_users
        get_room = Room.objects.filter(Q(users__in=users))

        #if the room already exists return it
        if get_room :
            room_name = get_room[0].room_name

        #else create a new room
        else :
            new_room = "_".join(sorted([str(user) for user in users]))

            """
            while True:
                room_exists = Room.objects.filter(room_name=new_room)
                if room_exists:
                    new_room = "_".join(sorted([str(sender_user), str(receiver_user)]))
                else :
                    break
            """
            #create_room = Room.objects.create(sender_user=sender_user, receiver_user=receiver_user, room_name=new_room)
            # Create the room instance first
            create_room = Room.objects.create(room_name=new_room)
            # Add users to the room
            for user in users:
                create_room.users.add(user)
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