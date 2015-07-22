#!/usr/bin/env python
import sys, os
import requests

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Genres


response = requests.get('https://freemusicarchive.org/api/get/genres.json?api_key=Q7W54CRBAQS4CEPZ')

response_dict = response.json()


for data in response_dict['dataset']:
    if data.get('genre_title') != None:
        genre, created = Genres.objects.get_or_create(genre_id=int(data.get('genre_id')))
        genre.genre_slug = str(data.get('genre_handle'))
        genre.genre_title = str(data.get('genre_title'))

        if data.get('genre_parent_id') != None:
            genre_parent, created = Genres.objects.get_or_create(genre_id=int(data.get('genre_parent_id')))
            genre.genre_parent_id = genre_parent

        genre.save()