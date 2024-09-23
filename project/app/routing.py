from django.urls import path, re_path, include
from app.consumer import ChatConsumer

# the empty string routes to ChatConsumer, which manages the chat functionality.
websocket_urlpatterns = [
    path(re_path(r'ws/chat/(?P<room_name>\w+)/$'), ChatConsumer.as_asgi()),
    #path("", ChatConsumer.as_asgi()),
]