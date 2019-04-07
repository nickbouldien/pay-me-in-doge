from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Site


def home(request):
    context = {"sites": Site.objects.all().order_by("upvotes")}
    return render(request, "board/home.html", context)


class SiteListView(ListView):
    model = Site
    template_name = "board/home.html"
    context_object_name = "sites"
    ordering = ["-upvotes"]


class SiteDetailView(DetailView):
    model = Site


def about(request):
    return render(request, "board/about.html")
