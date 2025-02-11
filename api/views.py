from django.shortcuts import render
from django.http import HttpResponse
import string
import random
# Create your views here.
def generate_password(request,length=15):
    characters=string.ascii_letters+string.digits
    password=''.join(random.choice(characters) for _ in range(length))
    return HttpResponse('your password:'+password)