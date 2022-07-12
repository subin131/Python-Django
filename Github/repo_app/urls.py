from repo_app import views
from django.urls import path,include

urlpatterns = [
    
    path("home/",views.home)
]
