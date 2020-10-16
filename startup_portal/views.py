from django.http import HttpResponse
from django.shortcuts import render 
from .config import firebaseConfig
import pyrebase

firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

def login(request):
   return render(request,"login.html")
def tempView(request):
   return HttpResponse("hello world")

def registerStartup(request):  
    return render(request, "register.html") 
