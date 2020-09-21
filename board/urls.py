from django.urls import path

from . import views
from .views import (
    SiteCreateView,
    SiteDeleteView,
    SiteDetailView,
    SiteListView,
    SiteUpdateView,
    UserSiteListView,
)

urlpatterns = [
    path("", SiteListView.as_view(), name="board-home"),
    path("about/", views.about, name="board-about"),
    path("resources/", views.resources, name="board-resources"),
    path("site/<int:pk>/", SiteDetailView.as_view(), name="site-detail"),
    path("site/<int:pk>/delete/", SiteDeleteView.as_view(), name="site-delete"),
    path("site/<int:pk>/update/", SiteUpdateView.as_view(), name="site-update"),
    path("site/new/", SiteCreateView.as_view(), name="site-create"),
    path("site/vote/", views.vote, name="site-vote"),  # ajax
    path("user/<str:username>/", UserSiteListView.as_view(), name="user-sites"),
]
