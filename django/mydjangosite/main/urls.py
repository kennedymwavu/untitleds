from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("v1/", views.v1, name = "view 1"), 
    path("v2/", views.v2, name = "view 2"), 
    path("v3/", views.v3, name = "view 3"), 
]