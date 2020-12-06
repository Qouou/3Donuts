from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.model, name='index'),
    #url(r'^download/',views.download,name="download"),
    #path('', views.head, name='head'),
    #url('Try/', views.add),
]
