from django.urls import path
from auth_app import views

urlpatterns = [
    path("home/", views.home),
]
