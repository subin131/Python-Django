from django.urls import path
from login_app import views

urlpatterns = [
    path("about/", views.about),
]
