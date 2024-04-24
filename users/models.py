from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from frontend.models import Album, Song, Artist  

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    """
    
    def __str__(self):
        return self.username


class UserCollection(models.Model):
    """
    Model to represent a user's music collection.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    albums = models.ManyToManyField(Album, blank=True, related_name='user_collections')
    songs = models.ManyToManyField(Song, blank=True, related_name='user_collections')
    artists = models.ManyToManyField(Artist, blank=True, related_name='user_collections')

    def __str__(self):
        return f"{self.user.username}'s collection"
