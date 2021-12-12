from django.urls import path
from . import views

URLPatterns = [
    path('', views.post_list, name='post_list'),
]