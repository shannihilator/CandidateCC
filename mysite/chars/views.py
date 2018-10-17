from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
import requests
import json

def chars(request):
	headers = {'Authorization':'Bearer ' + settings.SALESLOFT_API_KEY, 'Content-Type': 'application/json'}
	response = requests.get(settings.BASE_API_URL + '/people.json', headers=headers)
	data = response.json()

	# characters are stored in a dictionary {"character":frequency}
	characters={}
	for ids in data[u'data']:
		email = ids['email_address']
		for chars in email:
			keys = characters.keys()
			if chars in keys:
				characters[chars]+=1
			else: 
				characters[chars]=1

	# sort the characters dicitionary and store in a list if lists (2d array)
	sortedChars = []
	sortedChars.append([]) 
	for key, value in sorted(characters.iteritems(), key=lambda (k,v): (v,k), reverse=True):
		sortedChars[-1].append(key)
		sortedChars[-1].append(value)
		sortedChars.append([])

	return render(request, 'chars/count.html', {'characters':sortedChars})