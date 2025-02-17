from django.shortcuts import render
from django.http import HttpResponse
import string
import random
import requests
# Create your views here.
def generate_password(request,length=15):
    characters=string.ascii_letters+string.digits
    password=''.join(random.choice(characters) for _ in range(length))
    return HttpResponse('your password:'+password)
def kerman_weather(request):
    url="https://wttr.in/kerman?format=j1"
    response=requests.get(url)
    response.raise_for_status()
    info=response.json()
    temperature= info['current_condition'][0]['temp_C']
    return HttpResponse("weather informain collected:"+str(temperature)+"^C")
    