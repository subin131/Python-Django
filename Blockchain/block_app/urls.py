from block_app import views
from django.urls import path

urlpatterns = [
    path("home/",views.home)
]
