from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
import requests
import json

def people(request):
    headers = {'Authorization':'Bearer ' + settings.SALESLOFT_API_KEY, 'Content-Type': 'application/json'}
    response = requests.get(settings.BASE_API_URL + '/people.json', headers=headers)
    data = response.json()
    return render(request, 'people/list.html', {'people':data[u'data']})