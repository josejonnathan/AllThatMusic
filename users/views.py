from .forms import CustomUserCreationForm, CustomLoginForm
from django.shortcuts import get_object_or_404, redirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import UserCollection, User
from frontend.models import Album, Artist, Song
from django.urls import reverse_lazy

class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    

class UserLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    
# Collection creation
    
@receiver(post_save, sender=User)
def create_user_collection(sender, instance, created, **kwargs):
    if created:
        UserCollection.objects.create(user=instance)
        
@method_decorator(login_required, name='dispatch')
class UserCollectionDetailView(DetailView):
    model = UserCollection
    template_name = 'user_collection_detail.html'
    
@method_decorator(login_required, name='dispatch')
class UserCollectionArtistView(DetailView):
    model = UserCollection
    template_name = 'user_collection/artist_list.html'
    
    def get_object(self):
        return get_object_or_404(UserCollection, user=self.request.user)
    
@method_decorator(login_required, name='dispatch')
class UserCollectionAlbumView(DetailView):
    model = UserCollection
    template_name = 'user_collection/album_list.html'
    
    def get_object(self):
        return get_object_or_404(UserCollection, user=self.request.user)
    
@method_decorator(login_required, name='dispatch')
class UserCollectionSongView(DetailView):
    model = UserCollection
    template_name = 'user_collection/song_list.html'
    
    def get_object(self):
        return get_object_or_404(UserCollection, user=self.request.user)

# Collection Handling 

def get_user_collection(request):
    collection = get_object_or_404(UserCollection, user=request.user)
    return collection

@require_POST
@login_required
def add_album_to_collection(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    collection, _ = UserCollection.objects.get_or_create(user=request.user)
    collection.albums.add(album)
    if album.artist:
        collection.artists.add(album.artist)

    return redirect('user_collection_detail', collection.pk)

@require_POST
@login_required
def remove_album_from_collection(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    collection = UserCollection.objects.get(user=request.user)
    collection.albums.remove(album)

    return redirect('user_collection_detail', collection.pk)


@require_POST
@login_required
def add_song_to_collection(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    collection, _ = UserCollection.objects.get_or_create(user=request.user)
    collection.songs.add(song)
    if song.album:
        collection.albums.add(song.album)
    if song.artist:
        collection.artists.add(song.artist)
    return redirect('user_collection_detail', collection.pk)

@require_POST
@login_required
def remove_song_from_collection(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    collection = get_object_or_404(UserCollection, user=request.user)
    collection.songs.remove(song)
    return redirect('user_collection_detail', collection.pk)

@require_POST
@login_required
def add_artist_to_collection(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    collection, _ = UserCollection.objects.get_or_create(user=request.user)
    collection.artists.add(artist)
    return redirect('user_collection_detail', collection.pk)

@require_POST
@login_required
def remove_artist_from_collection(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    collection = get_object_or_404(UserCollection, user=request.user)
    collection.artists.remove(artist)
    return redirect('user_collection_detail', collection.pk)