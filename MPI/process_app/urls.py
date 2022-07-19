
from django.urls import path
from process_app import views
urlpatterns = [
    path('home/', views.home),
]
