from django.urls import path
from . import views


urlpatterns = [
    path('<int:phone_id>/add', views.add_to_cart, name='add'),
    path('view/', views.view, name='cartView'),
    path('<int:phone_id>/delete', views.delete, name='delete'),
]
    
