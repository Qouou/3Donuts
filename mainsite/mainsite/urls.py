"""mainsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account.views import login,logout,register,list_restaurants
from django.contrib.auth import views
from donuts.views import index, model, add, pifu
from django.conf.urls import url
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('index/', index),
    path('accounts/login/', login),
    path('index/', index),
    path('Try/', model),
    path('Try/add', add),
    path('Try/pifu', pifu),
    #path('accounts/login/', views.LoginView.as_view()),
    path('accounts/logout/', logout),
    path('accounts/register/', register),
    #url(r'^download/',download,name="download"),
    path('restaurants_list/', list_restaurants),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
