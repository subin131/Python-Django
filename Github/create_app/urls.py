from create_app import views
from django.urls import path,include

urlpatterns = [
    path("create/",views.create)
]
