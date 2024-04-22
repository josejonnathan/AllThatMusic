from django.db import models



class Artist(models.Model):
    """
    Model to store information about music artists.
    """
    name = models.CharField(max_length=100, unique=True,
                            help_text="Name of the artist")
    photo_url = models.URLField(
        max_length=200, null=True, help_text="URL of the artist's photo")
    photo = models.ImageField(null=True, blank=True,
                              upload_to='artist_photos/', help_text="Artist's photo")
    review = models.TextField(help_text="Review of the artist")
    youtube_link = models.URLField(
        help_text="Artist's YouTube link", null=True, blank=True)
    deezer_link = models.URLField(help_text="Artist's Deezer link", null=True)
    instagram_link = models.URLField(
        help_text="Artist's Instagram link", null=True, blank=True)

    def __str__(self):
        """
        Method to get the string representation of the artist.
        """
        return self.name


class Album(models.Model):
    """
    Model to store information about music albums.
    """
    title = models.CharField(max_length=100, help_text="Title of the album")
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='albums',
        help_text="Artist of the album"
    )

    year = models.PositiveIntegerField(help_text="Release year of the album")
    cover_url = models.URLField(
        max_length=200, null=True, help_text="URL of the album cover")
    main_cover = models.ImageField(
        upload_to='album_covers/', help_text="Main cover of the album", null=True, blank=True)
    tracklist = models.JSONField(
        help_text="List of songs in the album in JSON format")
    comments = models.TextField(
        help_text="Additional comments about the album")
    deezer_album_link = models.URLField(
        help_text="Albums's Deezer link", null=True)

    def __str__(self):
        """
        Method to get the string representation of the album.
        """
        return f'{self.title}'


class Song(models.Model):
    """
    Model to store information about songs in albums.
    """
    song = models.CharField(max_length=100, help_text="Title of the song")
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, help_text="Album to which the song belongs"
    )
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, help_text="Artist of the song"
    )
    lyrics = models.TextField(help_text="Lyrics of the song")
    youtube_link = models.URLField(
        help_text="YouTube link of the song", null=True, blank=True)
    deezer_link = models.URLField(
        help_text="Deezer link of the song", null=True)

    def __str__(self):
        """
        Method to get the string representation of the song.
        """
        return f"{self.song}"
