from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .models import Site
from users.models import Profile


def about(request):
    return render(request, "board/about.html")


def home(request):
    context = {"sites": Site.objects.all().order_by("vote_score")}
    return render(request, "board/home.html", context)


def resources(request):
    return render(request, "board/resources.html")


@require_POST
def vote(request):
    site_id = request.POST.get("siteId", None)
    vote = request.POST.get("vote", None)

    print("site_id: ", site_id)
    print("vote: ", vote)

    return JsonResponse({"post": "good"})


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


@method_decorator(ensure_csrf_cookie, name="dispatch")
class SiteListView(ListView):
    model = Site
    template_name = "board/home.html"
    context_object_name = "sites"
    ordering = ["-vote_score"]
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
        return Site.objects.filter(poster=user).order_by("-vote_score")

    def get_context_data(self, **kwargs):
        context = super(UserSiteListView, self).get_context_data(**kwargs)
        # TODO - can I access the user without having to do this twice??
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        context["profile"] = get_object_or_404(Profile, user_id=user.id)
        return context
