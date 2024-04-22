from django.contrib import admin
# from .models import Artist, Album, Song
from . import models


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'instagram_link', 'youtube_link']
    list_editable = ['instagram_link', 'youtube_link']

    search_fields = ['name']


@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist']
    search_fields = ['title', 'artist']


@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song', 'album', 'artist']
    search_fields = ['song', 'album', 'artist']
    list_per_page = 20
