from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .models import Site


def home(request):
    context = {"sites": Site.objects.all().order_by("upvotes")}
    return render(request, "board/home.html", context)


class SiteCreateView(LoginRequiredMixin, CreateView):
    model = Site
    fields = ["name", "link", "description"]

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)


class SiteDetailView(DetailView):
    model = Site


class SiteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Site
    success_url = "/"

    def test_func(self):
        site = self.get_object()
        if self.request.user == site.poster:
            return True
        return False


class SiteListView(ListView):
    model = Site
    template_name = "board/home.html"
    context_object_name = "sites"
    ordering = ["-upvotes"]


class SiteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Site
    fields = ["name", "link", "description"]

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

    def test_func(self):
        site = self.get_object()
        if self.request.user == site.poster:
            return True
        return False


def about(request):
    return render(request, "board/about.html")


def resources(request):
    return render(request, "board/resources.html")
