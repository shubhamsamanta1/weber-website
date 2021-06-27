from os import pardir
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from .models import Contact
from . models import Product
from math import ceil

def index(request):
    return render(request,'main.html')

def home(request):
    productss = reversed(Product.objects.all())
    return render(request, 'home.html',{'productss': productss})

def home1(request):
    productss = reversed(Product.objects.all().filter(category = "Comic"))
    return render(request, 'home1.html',{'productss': productss})

def home2(request):
    productss = reversed(Product.objects.all().filter(category = "Novel"))
    return render(request, 'home2.html',{'productss': productss})

def home3(request):
    productss = reversed(Product.objects.all().filter(category = "Story"))
    return render(request, 'home3.html',{'productss': productss})

def home4(request):
    productss = reversed(Product.objects.all().filter(category = "Autobiography"))
    return render(request, 'home4.html',{'productss': productss})

def home5(request):
    productss = reversed(Product.objects.all().filter(category = "Educational"))
    return render(request, 'home5.html',{'productss': productss})

def home6(request):
    productss = reversed(Product.objects.all().filter(category = "Motivational"))
    return render(request, 'home6.html',{'productss': productss})


def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method =='POST':
        name = request.POST.get('name','')
        email= request.POST.get('email','')
        phone= request.POST.get('phone','')
        query= request.POST.get('query','')
        contact =Contact(name=name, phone=phone, email=email, query=query, date=datetime.today())
        contact.save()
        messages.success(request,"Your query is been submitted. Thank your writing us we will reach you shortly")
    return render(request,'contact.html')

def signup(request):
     if request.method =='POST':
        username = request.POST['username']
        name = request.POST['name']
        last = request.POST['last']
        email= request.POST['email']
        password= request.POST['password']

        if User.objects.filter(username=username).exists():
            
            messages.success(request,"username exists please go back and signup again with different username.")
            return redirect('index')
        
        if User.objects.filter(email=email).exists():

            messages.success(request,"email id is used please go back and signup again with different email.")
            return redirect('index')

        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.first_name = name
        myuser.last_name = last
        myuser.save()
        messages.success(request,"Congrats, your account is sucesfully created please signin onto your account")
        return redirect('index')
     
     return redirect('index')


def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"logged in")
            return redirect("home")
        else:
            messages.success(request,"No user found please go back and signin again & if new kindly signup first")
            return redirect('index')
    
    return redirect('index')

def signout(request):
        logout(request)
        messages.success(request,"You have succesfully signout")
        return redirect('index')
        
    