from django.urls import path
from .views import (
    SiteCreateView,
    SiteDeleteView,
    SiteDetailView,
    SiteListView,
    SiteUpdateView,
)
from . import views

urlpatterns = [
    path("", SiteListView.as_view(), name="board-home"),
    path("site/<uuid:pk>/", SiteDetailView.as_view(), name="site-detail"),
    path("site/<uuid:pk>/update/", SiteUpdateView.as_view(), name="site-update"),
    path("site/<uuid:pk>/delete/", SiteDeleteView.as_view(), name="site-delete"),
    path("site/new/", SiteCreateView.as_view(), name="site-create"),
    path("about/", views.about, name="board-about"),
    path("resources/", views.resources, name="board-resources"),
]
