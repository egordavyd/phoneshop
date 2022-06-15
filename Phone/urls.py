from django.urls import path
from . import views


urlpatterns = [
    path('catalog/', views.index),
    path('<int:phone_id>/view', views.phone, name='view'),
    path('<int:phone_id>/buy', views.buy_phone, name='buy')
    ]

