from django.urls import path, re_path, include
from app.consumer import ChatConsumer

# the empty string routes to ChatConsumer, which manages the chat functionality.
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<roomName>\w+)/$', ChatConsumer.as_asgi()),
    #path("", ChatConsumer.as_asgi()),
]