
from django.shortcuts import render, redirect,HttpResponseRedirect,HttpResponse
from django.contrib import messages, auth 
from django.contrib.auth.models import User
from django.conf import settings
import os 
from .models import Uploads


def index(request):
    return render(request,'LoudLabel/index.html')

def about(request):
    return render(request,'LoudLabel/about.html')

def contact(request):
    return render(request,'LoudLabel/contact.html')

def product(request):
    return render(request,'LoudLabel/product.html')


def register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('LoudLabel:register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('LoudLabel:register')
        else:
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
        
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('LoudLabel:login')
    else:
      messages.error(request, 'Passwords dont match')
      return redirect('LoudLabel:register')
  else:
    return render(request, 'LoudLabel/register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are logged in')
      return redirect('LoudLabel:index')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('LoudLabel:login')
  else:
    return render(request, 'LoudLabel/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('LoudLabel:login')

def post(request):
  image=Uploads.objects.all()
  return render(request,"LoudLabel/loads.html",{"images":image}) 
          
          
def vids(request):
  vids=Uploads.objects.all()
  return render(request,"LoudLabel/vids.html",{"vids":vids})
    
def search(request):
  if request.method=="POST":
    search=request.POST["search"]
    searche=Uploads.objects.filter(title=search)
    return render(request,"LoudLabel/search.html",{"search":search,"searche":searche})
  else:
    return render(request,"LoudLabel/search.html")
  
                
def dashboard(request):
  return redirect("LoudLabel:index")
    

# Create your views here.
