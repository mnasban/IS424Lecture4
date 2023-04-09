from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("saad", views.saad, name="saad"),
     path("fahad", views.fahad, name="fahad")
 ]