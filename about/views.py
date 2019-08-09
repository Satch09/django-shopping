from django.shortcuts import render
from django.http import HttpResponse

# Create your views here


def about_view(*args, **kwargs):
    return HttpResponse('<h1>This is the about view</h1>')
