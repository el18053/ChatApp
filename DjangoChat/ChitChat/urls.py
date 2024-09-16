from django.urls import path, include
from ChitChat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView
#from .views import create_room, group_chat

urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),

    # authentication section
    path("auth/login/", LoginView.as_view(template_name="chat/loginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    path('group-chat/', chat_views.group_chat, name='group_chat'),
    path('create-room/', chat_views.create_room, name='create_room'),
    path('chat-room/<int:room_id>/', chat_views.chat_room, name='chat_room'),
]