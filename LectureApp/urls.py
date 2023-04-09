from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("<str:name>", views.greet,name="greet"),
     path("saad", views.saad, name="saad"),
     path("fahad", views.fahad, name="fahad")
 ]