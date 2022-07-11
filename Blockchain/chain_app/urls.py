
from django.urls import path,include
from chain_app import views
urlpatterns = [
    path("home/",views.home)
]
