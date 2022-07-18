from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('phones/', views.Phone_list.as_view()),
    path('phones/<int:pk>/', views.Phone_detail.as_view()),
]