from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
import pyrebase
from .config import firebaseConfig

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
from .forms import RegisterForm,LoginForm
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
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user=auth.sign_in_with_email_and_password(email,password)
            if user:
                messages.success(request, f'login successful')
                return render(request,'home.html',{})
            messages.failure(request,'invalid credentials')
    form=LoginForm()
    return render(request,'login.html',{'form':form})

def postLogin(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    user=auth.sign_in_with_email_and_password(email,password)
    return render(request,'home.html',{'user': user})


def basic(request):
    return render(request,'home.html',{})

