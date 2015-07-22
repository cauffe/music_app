from django.db import models

# Create your models here.


class Genres(models.Model):
    genre_id = models.IntegerField(null=True)
    genre_parent_id = models.ForeignKey('main.Genres', related_name='parent', null=True, db_index=True)
    genre_title = models.CharField(max_length=255, null=True)
    genre_slug = models.SlugField(max_length=255, null=True)

    def __unicode__(self):
        return "%s" % self.genre_title

class Artist(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    artist_url = models.CharField(max_length=255, null=True)
    artist_name = models.CharField(max_length=255, null=True)
    artist_bio = models.TextField(null=True)
    artist_location = models.CharField(max_length=255, null=True)
    artist_website = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return "%s" % self.artist_name

class Albums(models.Model):
    album_id = models.IntegerField(primary_key=True)
    artist = models.ForeignKey('main.Artist', null=True)
    album_title = models.CharField(max_length=255, null=True)
    album_date_released = models.DateField(null=True)
    album_image = models.ImageField(upload_to="album_images", null=True)

    def __unicode__(self):
        return self.album_title

class Tracks(models.Model):
    track_id = models.IntegerField(primary_key=True)
    album = models.ForeignKey('main.Albums', null=True)
    genre = models.ForeignKey('main.Genres', null=True)
    track_title = models.CharField(max_length=255, null=True)
    track_file = models.FileField(upload_to="tracks")

    def __unicode__(self):
        return self.track_title