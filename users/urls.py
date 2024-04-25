from django.urls import path
from .views import UserCollectionDetailView, UserRegisterView, UserLoginView, UserLogoutView, add_album_to_collection, remove_album_from_collection, add_song_to_collection, remove_song_from_collection, add_artist_to_collection, remove_artist_from_collection, UserCollectionArtistView, UserCollectionAlbumView, UserCollectionSongView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('collections/<int:pk>/', UserCollectionDetailView.as_view(), name='user_collection_detail'),
    path('add_album_to_collection/<int:album_id>/', add_album_to_collection, name='add_album_to_collection'),
    path('remove_album_from_collection/<int:album_id>/', remove_album_from_collection, name='remove_album_from_collection'),
    path('collection/add/song/<int:song_id>/', add_song_to_collection, name='add_song_to_collection'),
    path('collection/remove/song/<int:song_id>/', remove_song_from_collection, name='remove_song_from_collection'),
    path('collection/add/artist/<int:artist_id>/', add_artist_to_collection, name='add_artist_to_collection'),
    path('collection/remove/artist/<int:artist_id>/', remove_artist_from_collection, name='remove_artist_from_collection'),
    path('collections/artist/', UserCollectionArtistView.as_view(), name='user_collection_artist_list'),
    path('collections/album/', UserCollectionAlbumView.as_view(), name='user_collection_album_list'),
    path('collections/song/', UserCollectionSongView.as_view(), name='user_collection_song_list'),
    ]