from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("saad", views.index, name="index"),
     path("fahad", views.index, name="index")
 ]