from django.http import HttpResponse
from django.shortcuts import render 
import pyrebase

def tempView(request):
   return HttpResponse("hello world")

def registerStartup(request):  
    return render(request, "register.html") 
