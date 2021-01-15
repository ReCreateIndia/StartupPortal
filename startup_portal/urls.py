from django.contrib import admin
from django.urls import path,include
from .views import register,login,home,help,blog,addblog,registerUser,temp


urlpatterns = [
    path('register/',register),
    path('login/',login),
    path('',home),
    path('help/',help),
    path('blog/',blog),
    path('addblog/',addblog),
    path('registerUser/',registerUser),
    path('temp/',temp)
]
