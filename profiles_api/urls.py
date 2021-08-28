from django.urls import path
from profiles_api import views

urlpatterns = [
    path('user/', views.ApiViewController.as_view()),
]
