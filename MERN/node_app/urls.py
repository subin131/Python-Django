
from django.urls import path
from node_app import views
urlpatterns = [
   path("home/", views.home),
]
