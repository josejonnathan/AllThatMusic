import requests


def get_lyrics(artist, title):
    """
    Fetches the lyrics of a song using the Lyrics.ovh API.

    Args:
        artist (str): The name of the artist.
        title (str): The title of the song.

    Returns:
        str: The lyrics of the song, or None if not found.
    """
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        lyrics = data.get('lyrics')
        # Split the lyrics by lines and exclude the first line
        lyrics_lines = lyrics.split('\n')[1:]
        # Join the remaining lines back together
        modified_lyrics = '\n'.join(lyrics_lines)
        return modified_lyrics
    else:
        return None
