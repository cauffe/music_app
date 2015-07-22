#!/usr/bin/env python
import sys, os
import requests
from unidecode import unidecode

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Artist

response = requests.get('https://freemusicarchive.org/api/get/artists.json?api_key=Q7W54CRBAQS4CEPZ&limit=200')

response_dict = response.json()


for data in response_dict['dataset']:

    artist, created = Artist.objects.get_or_create(artist_id=int(data.get('artist_id')))
    artist.artist_id = int(data.get('artist_id'))
    artist.artist_url = str(data.get('artist_url'))
    artist.artist_name = str(unidecode(data.get('artist_name')))

    if data.get('artist_bio') != None:
        artist.artist_bio = str(unidecode(data.get('artist_bio')))

    if data.get('artist_location') != None:
        artist.artist_location = str(unidecode(data.get('artist_location')))
    
    if data.get('artist_website') != None:
        artist.artist_website = str(data.get('artist_website'))
    artist.save()