from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .config import firebaseConfig,serviceAccount
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
from .forms import RegisterForm

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth,firestore

cred=credentials.Certificate('config.json.json')
firebase_admin.initialize_app(cred)

db=firestore.client()
user="bla"
def register(request):
    if request.method == 'POST':
        teamName=request.POST.get('team_name')
        db.collection('startups').document().set({
            'TeamName':teamName,
        
        })
        return render(request,'home.html')
    return render(request, 'register.html',{})

def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        email+='@gmail.com'
        password=request.POST.get('password')
        user=auth.create_user(email=email,password=password)
        db.collection('users').document().set({
            'username':email,
        
        })
        return render(request,'home.html')
    return render(request,'login.html',{})

def home(request):
    return render(request,'home.html',{'user': user})
def help(request):
    return render(request,'help.html',{'user': user})
def blog(request):
    docs = db.collection(u'shares').document(u'BEZqpYXndCRQTrqfJocB').collection(u'Bloging').stream()

    return render(request,'blog.html',{'docs': docs})
def basic(request):
    return render(request,'home.html',{})

