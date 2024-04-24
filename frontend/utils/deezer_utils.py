import requests
from ..models import Album, Artist, Song


def fetch_album_info_from_deezer(album_id):
    """
    Fetches album information from the Deezer API based on the provided album ID.

    Args:
        album_id (str): The ID of the album on Deezer.

    Returns:
        Album: The Album object created or updated in the database.
               None if there was an error fetching the album information.
    """
    # Base URL of the Deezer API
    base_url = "https://api.deezer.com/album/"

    # Construct the full URL to fetch album information
    url = f"{base_url}{album_id}"

    # Make the request to the Deezer API
    response = requests.get(url)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        album_data = response.json()
        
        if 'error' in album_data:
            print(f"Error al obtener el álbum: {album_data['error']['message']}")
            return None
        
        else:
            

            # Extract album information
            title = album_data.get("title")
            artist_name = album_data.get("artist", {}).get("name")
            year = album_data.get("release_date")[:4]  # Get only the year
            cover_url = album_data.get("cover_big")
            photo_url = album_data.get("artist", {}).get("picture_big")
            deezer_album_link = album_data.get("link")
            deezer_artist_link = None
            contributors = album_data.get("contributors", [])
            for contributor in contributors:
                if contributor.get("name") == artist_name:
                    deezer_artist_link = contributor.get("link")
                    break

            # Extract song information from the tracklist
            tracklist = album_data.get("tracks", {}).get("data", [])

            # Extract only the title of each track
            tracklist_titles = [track.get("title") for track in tracklist]

            # Check if the artist already exists in the database
            artist, created = Artist.objects.get_or_create(
                name=artist_name,
                photo_url=photo_url,
                deezer_link=deezer_artist_link
            )

            # Create or update the album
            album, created = Album.objects.update_or_create(
                title=title,
                artist=artist,
                year=year,
                cover_url=cover_url,
                deezer_album_link=deezer_album_link,
                # Update the tracklist with only the titles
                defaults={"tracklist": tracklist_titles}
            )

            # Create songs for each track in the tracklist
            for track in tracklist:
                song_title = track.get("title")
                song_deezer_link = track.get("link")
                # For simplicity, let's assume we don't have lyrics or YouTube links for now
                Song.objects.get_or_create(
                    song=song_title,
                    album=album,
                    artist=artist,
                    deezer_link=song_deezer_link
                )

            return album
    else:
        
        # If the request was not successful, print the HTTP status code

        return 'Album not found'
