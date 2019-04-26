from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
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
from functools import wraps
from common.util.decorators import ajax_login_required
from users.models import Profile
from .forms import SiteCreateForm, SiteUpdateForm
from .models import Site

votes = {"DOWNVOTE": -1, "UPVOTE": 1, "DELETE": 0}

MIN_VOTE_SCORE = -5


def about(request):
    return render(request, "board/about.html")


def resources(request):
    return render(request, "board/resources.html")


@ajax_login_required
@require_POST
def vote(request):
    site_id = request.POST.get("siteId", None)
    vote = request.POST.get("vote", None)

    if not site_id or not vote:
        return JsonResponse({"message": "site_id and vote are required."}, status=400)

    site = get_object_or_404(Site, pk=site_id)

    # dont let the user vote for their own site
    if site.poster.id == request.user.id:
        return JsonResponse({"message": "can't vote for your own site"}, status=400)

    try:
        vote_num = int(vote)
        if vote_num == votes["UPVOTE"]:
            site.votes.up(request.user.id)
        elif vote_num == votes["DOWNVOTE"]:
            site.votes.down(request.user.id)
        elif vote_num == votes["DELETE"]:
            site.votes.delete(request.user.id)
        else:
            return JsonResponse({"message": "vote must be -1, 0, or 1"}, status=400)
    except:
        return JsonResponse(
            {"message": f"error registering vote {vote} for site with id {site_id}"},
            status=400,
        )

    return JsonResponse(
        {"message": f"registered vote {vote} for site with id {site_id}"}
    )


class SiteCreateView(LoginRequiredMixin, CreateView):
    model = Site
    form_class = SiteCreateForm

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)


class SiteDetailView(DetailView):
    model = Site
    context_object_name = "site"

    def get_context_data(self, **kwargs):
        context = super(SiteDetailView, self).get_context_data(**kwargs)

        site = get_object_or_404(Site, pk=self.kwargs["pk"])

        vote = 0  # default (they didn't vote on the site or deleted their vote)
        if self.request.user.is_authenticated:
            check = {"user_id": self.request.user.id}
            user_votes_up = site.votes.user_ids(0)
            user_votes_down = site.votes.user_ids(1)

            if check in user_votes_up.values("user_id"):
                vote = 1
            elif check in user_votes_down.values("user_id"):
                vote = -1

        context["vote"] = vote
        return context


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
    paginate_by = 5

    def get_queryset(self):
        all_sites = Site.objects.filter(vote_score__gt=MIN_VOTE_SCORE).order_by(
            "-vote_score"
        )

        sites = []

        for site in all_sites:
            vote = 0  # default (they didn't vote on the site or deleted their vote)
            if self.request.user.is_authenticated:
                check = {"user_id": self.request.user.id}
                user_votes_up = site.votes.user_ids(0)
                user_votes_down = site.votes.user_ids(1)

                if check in user_votes_up.values("user_id"):
                    vote = 1
                elif check in user_votes_down.values("user_id"):
                    vote = -1

            site.vote = vote
            sites.append(site)

        return sites


class SiteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Site
    form_class = SiteUpdateForm
    template_name = "board/site.html"

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

        return Site.objects.filter(poster=user, vote_score__gt=MIN_VOTE_SCORE).order_by(
            "-vote_score"
        )

    def get_context_data(self, **kwargs):
        context = super(UserSiteListView, self).get_context_data(**kwargs)
        # TODO - can I access the user without having to do this twice??
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        context["profile"] = get_object_or_404(Profile, user_id=user.id)
        return context
