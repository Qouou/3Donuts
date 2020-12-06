from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django .contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from donuts.models import User_picture
# Create your views here.


def index(request):
    return render(request, 'index.html')

@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/index/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/Try/')
    else:
        return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())


@login_required
def list_restaurants(request):
    donuts_user_picture = User_picture.objects.all()
    return render(request,'restaurants_list.html', locals())
