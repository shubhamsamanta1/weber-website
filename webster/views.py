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

def error(request):
    context = {
        "variable1": "404 !!",
        "variable2": "Uh oh! Looks like you got lost.",
        "variable3": "Please go back and sign in."
    }
    return render(request, 'message.html', context)

def success(request):
    context = {
        "variable1": "Congrts !!",
        "variable2": "Your Account is been created succesfully.",
        "variable3": "Please go back and sign in."
    }
    return render(request, 'message.html', context)

def logerror(request):
    context = {
        "variable1": "Alert !!",
        "variable2": "Input error.",
        "variable3": "No user found please go back and signin again."
    }
    return render(request, 'message.html', context)

def usermatch(request):
    context = {
        "variable1": "Alert !!",
        "variable2": "Input error.",
        "variable3": "username exists please go back and signup again with different username."
    }
    return render(request, 'message.html', context)

def mailmatch(request):
    context = {
        "variable1": "Alert !!",
        "variable2": "Input error.",
        "variable3": "email id exists please go back and signup again with different email."
    }
    return render(request, 'message.html', context)

def signup(request):
     if request.method =='POST':
        username = request.POST['username']
        name = request.POST['name']
        last = request.POST['last']
        email= request.POST['email']
        password= request.POST['password']

        if User.objects.filter(username=username).exists():
            
            return redirect('usermatch')
        
        if User.objects.filter(email=email).exists():

            return HttpResponse("Input error -- Email Exists please to back and fill again")

        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.first_name = name
        myuser.last_name = last
        myuser.save()
        return redirect('success')
     
     return redirect('error')


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
            return redirect('logerror')
    
    return redirect('error')

def signout(request):
    if request.method =='POST':
        logout(request)
        return redirect('index')
        
    return redirect('error')