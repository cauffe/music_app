#!/usr/bin/env python
import sys, os
import requests
from unidecode import unidecode
from PIL import Image
from StringIO import StringIO

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from main.models import Albums, Artist, Genres

django.setup()

response = requests.get('http://freemusicarchive.org/api/get/albums.json?api_key=Q7W54CRBAQS4CEPZ&limit=10')

response_dict = response.json()

for data in response_dict['dataset']:
    print "IMAGE: %s" % data.get('album_image_file')
    print "TITLE: %s" % data.get('album_title')
    print "ARTIST: %s" % data.get('artist_name')
    print "ARTIST HANDLE: %s" % data.get('artist_handle')

    album, created = Albums.objects.get_or_create(album_id=int(data.get('album_id')))

    if data.get('album_title') != None:
        album.album_title = str(unidecode(data.get('album_title')))

    try:
        album_image = requests.get(data.get('album_image_file'))
        temp_image = NamedTemporaryFile(delete=True)
        temp_image.write(album_image.content)
        album.album_image = File(temp_image)
    except Exception, e:
        print e

    try:
        artist, created = Artist.objects.get_or_create(artist_name=data.get('artist_name'))
        album.artist = artist.pk
    except Exception, e:
        
        #https://freemusicarchive.org/api/get/artists.json?api_key=Q7W54CRBAQS4CEPZ&artist_handle=Duane_The_Teenage_Weirdo
        print e

    album.save()

