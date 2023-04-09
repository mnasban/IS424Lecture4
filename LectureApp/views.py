from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.

def index(request):
     return HttpResponse("Alsalam Alikum, world!")

def saad(request):
     return HttpResponse("Alsalam Alikum, Saad!")

def fahad(request):
     return HttpResponse("Alsalam Alikum, Fahad!")