from video_app import views
from django.urls import path

urlpatterns = [
    path('about/',views.about),
]
