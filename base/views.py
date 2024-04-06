from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.forms import UserCreationForm
from .models import MyModel
from .forms import MyForm


# Create your views here.

def loginpage(request):
    page="login"
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request,"User does not exists !")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Username or password does not exist")

    context = {'page': page}
    return render(request, 'base/index.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'An error has occured during registration')

    context ={'form': form}
    return render(request,'base/index.html', context)

def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'cv-form.html', {'form': form})

#index = homepage
def index(request):
    return render(request,'base/landing.html')

def about(request):
    return render(request,'base/about.html')

def r(request):
    return render(request,'base/ds.html')

def dep(request):
    return render(request,'base/ds.html')

def ngo(request):
    return render(request,'base/ngo.html')

def feed(request):
    return render(request,'base/feed.html')

def con(request):
    return render(request,'base/contact.html')

