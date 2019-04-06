from django.shortcuts import render
from .models import Site


def home(request):
    context = {"sites": Site.objects.all()}
    return render(request, "board/home.html", context)


def about(request):
    return render(request, "board/about.html")
