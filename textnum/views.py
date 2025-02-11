from django.shortcuts import render
from django.http import HttpResponse
import requests
import random
# Create your views here.
def number_text(request):
    NUMBER=random.randint(1,1000)
    url=f"http://numbersapi.com/{NUMBER}"
    response=requests.get(url)
    if response.status_code==200:
        return HttpResponse(response)
    else:
        return HttpResponse(response.status_code)