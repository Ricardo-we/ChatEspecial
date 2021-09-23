from django.db import models

# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=2000)
    
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"


class Messages(models.Model):
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.CharField(max_length=2000)
    room = models.CharField(max_length=2000)
    
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.user

class User(models.Model):
    user = models.CharField(max_length=2000)