from django.urls import path, include
from .views import HomePageView, DeezerRequestView, ArtistListView, ArtistDetailView, AlbumListView, AlbumDetailView, SongListView, SongDetailView, ArtistUpdateView, SongUpdateView, search_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create/', DeezerRequestView.as_view(), name='create_from_deezer'),
    path('artist/', ArtistListView.as_view(), name="artist_list"),
    path('album/', AlbumListView.as_view(), name="album_list"),
    path('song/', SongListView.as_view(), name="song_list"),
    path('artist/<int:pk>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('song/<int:pk>/', SongDetailView.as_view(), name='song_detail'),
    path('artist/update/<int:pk>/',
         ArtistUpdateView.as_view(), name='artist_update'),
    path('song/update/<int:pk>/',
         SongUpdateView.as_view(), name='song_update'),
    path('search/', search_view, name='search_view'),
]
