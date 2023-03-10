from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


app_name = "anasite"   


urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("resume", views.resume, name="resume"),
    path("contact", views.contact, name="contact")
]