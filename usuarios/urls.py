from django.contrib import admin
from django.urls import path
from .views import register, login

urlpatterns = [
    path('login/', login),
    path('register/', register),
]