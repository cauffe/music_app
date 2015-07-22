from django.shortcuts import render
from django.http import HttpResponse

import simplejson as json

import requests

# Create your views here.


def api_test2(request):

	response = requests.get('http://freemusicarchive.org/api/get/tracks.json?api_key=Q7W54CRBAQS4CEPZ&genre_handle=Rock&limit=20&page=3')

	response_dict = response.json()

	response_dict['dataset'][0].keys()

	count = 1
	for data in response_dict['dataset']:
		print type(data)
		for k, v in data.items():
			#print k
			if k == 'track_title' or k == 'artist_name':
				count += 1
				print "key: %s , value: %s, count: %s" % (k,v, count)
			

	return HttpResponse("%s" % response_dict['dataset'][0]['album_title'])