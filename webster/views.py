from os import pardir
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request,'main.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def signup(request):
     if request.method =='POST':
        username = request.POST['username']
        name = request.POST['name']
        last = request.POST['last']
        email= request.POST['email']
        password= request.POST['password']

        if User.objects.filter(username=username).exists():
            
            return HttpResponse("Input error -- Username Exists please to back and fill again")
        
        if User.objects.filter(email=email).exists():

            return HttpResponse("Input error -- Email Exists please to back and fill again")

        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.first_name = name
        myuser.last_name = last
        myuser.save()
        messages.success(request,"Your Account Has Been Created Succesfully")
        return redirect('home')
     
     return HttpResponse('404 - Not Allowed')


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
            return HttpResponse('Input error -- No user found please fo back and fill again')
    
    return HttpResponse('404 - Not Allowed')

def signout(request):
    if request.method =='POST':
        logout(request)
        return redirect('index')
        
    return HttpResponse('404 - Not Allowed')