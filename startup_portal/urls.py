from django.contrib import admin
from django.urls import path,include
from .views import register,login,home,help,blog,addblog


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register),
    path('login/',login),
    path('home/',home),
    path('home/help/',help),
    path('home/blog/',blog),
    path('home/addblog/',addblog),
]
