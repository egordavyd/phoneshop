from unicodedata import name
from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('create/', views.register, name='register'),
    path('createGen/', views.register2, name='register2'),
    path('profile/', views.profile, name='profile')
]