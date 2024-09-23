from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def index(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    # Get all users
    users = User.objects.filter(is_superuser=False)

    context = {
        'users': users  # Pass users to the template
    }
    return render(request, "index.html", context)

def chatPage(request, roomName, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {
        "roomName" : roomName
    }
    return render(request, "chatPage.html", context)