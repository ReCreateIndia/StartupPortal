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
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            team_name = form.cleaned_data.get('team_name')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

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


def basic(request):
    return render(request,'home.html',{})

