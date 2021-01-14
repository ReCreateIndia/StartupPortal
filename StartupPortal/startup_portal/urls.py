from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import register,login,home,help,blog,addblog,registerUser,temp,logout,forgot,detail


urlpatterns = [
    path('register/',register),
    path('login/',login),
    path('',home),
    path('help/',help),
    path('blog/',blog),
    path('addblog/',addblog),
    path('registerUser/',registerUser),
    path('temp/',temp),
    path('logout/',logout),
    path('forgot/',forgot),
    path('detail/',detail)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)