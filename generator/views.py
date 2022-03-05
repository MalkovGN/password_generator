from django.shortcuts import render
from django.http import HttpResponse
import string
import random


# Create your views here.

def home(request):
    return render(request, "generator/home.html")


def page1(request):
    return HttpResponse('<h1>This is the first page of my site!</h1>')


def page2(request):
    return HttpResponse('<h1>This is the second page of my site!</h1>')


def password(request):
    characters = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()?><'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {'password': thepassword})


def site_description(request):
    return render(request, "generator/site_description.html")