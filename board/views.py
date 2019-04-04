from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<p>hello, world!</p>")


def about(request):
    return HttpResponse("<p>about paymeindoge</p>")
