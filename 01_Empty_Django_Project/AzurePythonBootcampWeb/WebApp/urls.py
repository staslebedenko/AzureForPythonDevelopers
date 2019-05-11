from django.urls import path
from WebApp import views

urlpatterns = [
    path("", views.home, name="home"),
]