from django.core.paginator import Paginator
from django.db.models import Count
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import UpdateView
from .utils.deezer_utils import fetch_album_info_from_deezer
from .models import Artist, Album, Song
from .utils.lyrics import get_lyrics


class DeezerRequestView(TemplateView):
    """
    View for fetching album information from Deezer.
    """
    template_name = "create_from_deezer.html"

    def get_context_data(self, **kwargs):
        """
        Get context data for the template.

        Returns:
            dict: Context data for the template.
        """
        context = super().get_context_data(**kwargs)
        album_id = self.request.GET.get('album_id')

        if album_id:
            album = fetch_album_info_from_deezer(album_id)
            if album:
                context['album'] = album
                # Iterate through songs in the album
                for song in album.song_set.all():
                    # Fetch lyrics for the song
                    lyrics = get_lyrics(song.artist.name, song.song)
                    if lyrics:
                        # Assign lyrics to the song
                        song.lyrics = lyrics
                        # Save the updated song object
                        song.save()
                    else:
                        song.lyrics = "Lyrics not found for this song."
            else:
                # Handle the case when the album is not found
                context['error_message'] = "Album not found on Deezer."
        return context

    def dispatch(self, request, *args, **kwargs):
        """
        Dispatch method to handle the request.

        Args:
            request: HTTP request object.
            args: Additional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: HTTP response.

        Notes:
            Checks if album_id is present in the request. If not, continues without redirection.
        """
        # Check if album_id is present in the request
        album_id = self.request.GET.get('album_id')
        if not album_id:
            # If album_id is not present, continue without redirection
            return super().dispatch(request, *args, **kwargs)

        return super().dispatch(request, *args, **kwargs)


class HomePageView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        random_albums = Album.objects.order_by('?')[:3]

        context['random_albums'] = random_albums
        return context


class ArtistListView(ListView):
    model = Artist
    template_name = 'artist_list.html'  # Template for rendering the list
    context_object_name = 'artists'  # Name of the context variable in the template
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        artists_by_album_count = Artist.objects.annotate(
            num_albums=Count('albums')).order_by('-num_albums')
        context['artists_by_album_count'] = artists_by_album_count

        return context


class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artist_detail.html'
    context_object_name = 'artist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist = self.object
        albums = Album.objects.filter(song__artist=artist).distinct()
        context['albums'] = albums
        return context


class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'  # Template for rendering the list
    context_object_name = 'albums'  # Name of the context variable in the template
    ordering = ['title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener la lista de álbumes ordenados por año
        albums_by_year = Album.objects.annotate(
            num_years=Count('year')).order_by('-year')
        context['albums_by_year'] = albums_by_year

        return context


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album_detail.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.object
        # Obtener todas las canciones del álbum
        context['songs'] = album.song_set.all()
        context['artist_detail_url'] = reverse(
            'artist_detail', kwargs={'pk': album.artist.pk})
        return context


class SongListView(ListView):
    model = Song
    template_name = 'song_list.html'
    context_object_name = 'songs'
    ordering = ['song']
    paginate_by = 20  # Specify the number of songs per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist_list = context[self.context_object_name]
        artists_with_most_songs = Artist.objects.annotate(
            num_songs=Count('song')).order_by('-num_songs')[:15]  # Obtener los primeros 5 artistas
        context['artists_with_most_songs'] = artists_with_most_songs
        paginator = Paginator(artist_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['songs'] = page_obj
        return context


class SongDetailView(DetailView):
    model = Song
    template_name = 'song_detail.html'
    context_object_name = 'song'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        song = self.object
        album_cover_url = song.album.cover_url
        artist_photo_url = song.artist.photo_url
        # Agregar el enlace al ArtistDetailView relacionado
        context['artist_detail_url'] = reverse(
            'artist_detail', kwargs={'pk': song.artist.pk})
        # Agregar el enlace al AlbumDetailView relacionado
        context['album_detail_url'] = reverse(
            'album_detail', kwargs={'pk': song.album.pk})
        context['album_cover_url'] = album_cover_url
        context['artist_photo_url'] = artist_photo_url
        return context


class ArtistUpdateView(UpdateView):
    model = Artist
    fields = ['review', 'instagram_link', 'youtube_link']
    template_name = 'artist_update.html'
    success_url = reverse_lazy('artist_list')


class SongUpdateView(UpdateView):
    model = Song
    fields = ['lyrics', 'youtube_link']
    template_name = 'song_update.html'
    success_url = reverse_lazy('song_list')
