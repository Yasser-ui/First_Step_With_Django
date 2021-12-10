from django.urls import path
from django.urls import path
from . import views

URLPattern = [
    path('', views.post_list, name='post_list'),
]