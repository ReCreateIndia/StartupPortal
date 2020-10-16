from django.contrib import admin
from django.urls import path,include
from .views import register,login,postLogin,basic


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register),
    path('login/',login),
    path('postLogin/',postLogin),
    path('',basic)
]
