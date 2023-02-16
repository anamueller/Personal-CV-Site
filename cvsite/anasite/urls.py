from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


app_name = "anasite"   


urlpatterns = [
    path("", views.homepage, name="homepage")
]