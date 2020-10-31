from django.contrib import admin
from django.urls import path,include
from .views import register,login,home,help,blog


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register),
    path('login/',login),
    path('home/',home),
    path('help/',home),
    path('blog/',home),
]
