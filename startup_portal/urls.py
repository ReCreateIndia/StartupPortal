from django.contrib import admin
from django.urls import path,include
from .views import registerStartup,tempView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',registerStartup),
    path('',include('blog.urls'))
]
