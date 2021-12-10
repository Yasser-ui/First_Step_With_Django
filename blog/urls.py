from django.urls import path
from django.urls import path, re_path
from django.contrib import admin

from blog import views

URLPatterns = [
    path('', views.post_list, name='post_list'),
]