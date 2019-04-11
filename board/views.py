from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .models import Site


def about(request):
    return render(request, "board/about.html")


def home(request):
    context = {"sites": Site.objects.all().order_by("upvotes")}
    return render(request, "board/home.html", context)


def resources(request):
    return render(request, "board/resources.html")


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
    paginate_by = 5


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


class UserSiteListView(ListView):
    model = Site
    template_name = "board/user_sites.html"
    context_object_name = "sites"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Site.objects.filter(poster=user).order_by("-upvotes")
