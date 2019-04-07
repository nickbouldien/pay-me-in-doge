from django.urls import path
from .views import SiteDetailView, SiteListView
from . import views

urlpatterns = [
    path("", SiteListView.as_view(), name="board-home"),
    path("site/<uuid:pk>", SiteDetailView.as_view(), name="site-detail"),
    path("about/", views.about, name="board-about"),
]
