from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.db.models import SET

# Create your models here.
class Room(models.Model):
    """
    model for chat rooms
    """
    #sender_user = models.ForeignKey(User, related_name='room_sender', on_delete=SET(AnonymousUser.id))
    #receiver_user = models.ForeignKey(User, related_name='room_receiver', on_delete=SET(AnonymousUser.id))
    users = models.ManyToManyField(User, related_name='chatRooms')
    room_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.room_name