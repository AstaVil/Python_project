from django.db import models
from django.conf import settings

class Room(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    chat_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('chat_date',)
