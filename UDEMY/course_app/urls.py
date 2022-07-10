from django.urls import path
from course_app import views

urlpatterns = [
    path('home/', views.home),
]
