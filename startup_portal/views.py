from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.utils.datastructures import MultiValueDictKeyError
from .config import firebaseConfig,serviceAccount
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
from .forms import RegisterForm
config = {
    "apiKey": "AIzaSyDFtg_YkT7Ej_sCf63gRudcgjTGhkUwthU",
    "authDomain": "startupcarvaan.firebaseapp.com",
    "databaseURL": "https://startupcarvaan.firebaseio.com",
    "projectId": "startupcarvaan",
    "storageBucket": "startupcarvaan.appspot.com",
    "messagingSenderId": "844859435167",
    "appId": "1:844859435167:web:921c1da84bcdf026c89aaa",
    "measurementId": "G-MHFP9HXHE5"
    }
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase
cred=credentials.Certificate('config.json.json')
firebase_admin.initialize_app(cred)
firebase=pyrebase.initialize_app(config)
db=firestore.client()
auth=firebase.auth()
storage=firebase.storage()
email=""
password=""
def register(request):
    if request.method == 'POST':
        teamName=request.POST.get('team_name')
        db.collection('startups').document().set({
            'TeamName':teamName,
        
        })
        return render(request,'blog.html')
    return render(request, 'register.html',{})

def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=auth.sign_in_with_email_and_password(email, password)
        return redirect('/')
    return render(request,'login.html',{})

def home(request):
    if auth.current_user:
        auth.refresh(auth.current_user['refreshToken'])
        return render(request,'layout.html',{'id':auth.current_user['localId']})
    return redirect('/login/')
def help(request):
    return render(request,'help.html',{})
def blog(request):
    docs = db.collection(u'shares').document(u'BEZqpYXndCRQTrqfJocB').collection(u'Bloging').stream()
    return render(request,'blog.html',{'docs': docs})
def addblog(request):
    return render(request,'Add_blog.html',{})
def registerUser(request):
    return render(request,'form/form.html',{})

