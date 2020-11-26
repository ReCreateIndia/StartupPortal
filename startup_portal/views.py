from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.utils.datastructures import MultiValueDictKeyError
from .config import firebaseConfig,serviceAccount
from pathlib import Path
import os
from django.core.files.storage import FileSystemStorage 
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
    if request.method == 'POST' and request.FILES['file']:
        teamName=request.POST.get('teamname')
        email=request.POST.get('email')
        number=request.POST.get('phone')
        student=request.POST.get('student')
        professional=request.POST.get('professional')
        myfile = request.FILES['file']
        storage.child('startupFiles').child(email).put(myfile)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile) 
        db.collection('startups').document().set({
            'teamName':teamName,
            'email':email,
            'number':number,
            'student':student,
            'professional':professional,
            'filename':filename
        })
        return redirect('/temp')
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
        localId=auth.current_user['localId']
        data = db.collection(u'shares').document(localId).get()
        price = db.collection(u'shares').document(localId).collection("Price").document("price").get()
        return render(request,'home.html',{'id':"Home Page","data":data,"price":price})
    return redirect('/login/')
def help(request):
    return render(request,'help.html',{})
def temp(request):
    return render(request,'temp.html',{})
def blog(request):
    docs = db.collection(u'shares').document(u'BEZqpYXndCRQTrqfJocB').collection(u'Bloging').stream()
    return render(request,'blog.html',{'docs': docs})
def addblog(request):
    return render(request,'Add_blog.html',{})
def registerUser(request):
    if request.method == 'POST' and request.FILES['logoFile']:
        username=request.POST.get('email')
        password=request.POST.get('password')
        auth.create_user_with_email_and_password(username, password)
        auth.sign_in_with_email_and_password(username, password)
        localId=auth.current_user['localId']


        myfile = request.FILES['logoFile']
        storage.child('startupFiles').child(localId).put(myfile)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)


        storage.child("shareFiles").child(localId).child(filename).put(myfile)











        if auth.current_user:
            name=request.POST.get('companyName')
            special=request.POST.get('description')
            growth=request.POST.get('growth')
            introVideoUrl=request.POST.get('introVideoUrl')
            invest=request.POST.get('peopleInvested')
            tag=request.POST.get('tag')
            buyingPrice=request.POST.get('buyingPrice')
            occupied=request.POST.get('occupied')
            sellingPrice=request.POST.get('sellingPrice')
            totalShares=request.POST.get('totalShares')
            db.collection('shares').document(localId).set({
                'companyname':name,
                'description':special,
                'growth':growth,
                'id':auth.current_user['localId'],
                'introvideourl':introVideoUrl,
                'logoUrl':"shareFiles/"+auth.current_user['localId']+"/"+filename,
                'peopleinvested':invest,
                'tag':tag
            })
            db.collection('shares').document(localId).collection("Price").document("price").set({
                'buyingPrice':buyingPrice,
                'occupied':occupied,
                'sellingPrice':sellingPrice,
                'totalShares':totalShares

            })
            return redirect('/')
        else :
            return render(request,'login.html')
    return render(request,'registerstartup.html',{})

