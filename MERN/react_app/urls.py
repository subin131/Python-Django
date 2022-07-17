from django.urls import path
from react_app import views
urlpatterns = [
   path("home/", views.home),
]
