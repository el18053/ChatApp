# chatapp/urls.py
from django.urls import path
from .views import index, roomName
app_name = 'app'
urlpatterns = [
    path('', index, name="index"),
    path('<str:room_name>/', roomName, name='room'),
]