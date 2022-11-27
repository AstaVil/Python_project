from django.db import models

from django.conf import settings


class TaskPost(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)
    deadline = models.DateField('Galioja iki', null=True, blank=True)

    def __str__(self):
        return str(self.description)
