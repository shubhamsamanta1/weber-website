from os import pardir
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from .models import Contact
from . models import Product

def index(request):
    return render(request,'main.html')

def profile(request):
    users =request.user.username
    name = request.user.first_name
    last = request.user.last_name
    email = request.user.email
    context = {
        'user': users,
        'name': name,
        'last': last,
        'email' : email,
    }
    return render(request, 'profile.html', context)

def all(request):
    productss = reversed(Product.objects.all())
    variablemain = 'List of all books availble currently:'
    variable1 = 'All'
    variable2 = 'Comics'
    variable3 = 'Novel'
    variable4 = 'Story'
    variable5 = 'Autobiography'
    variable6 = 'Educational'
    variable7 = 'Motiational'
    link1 = '/all'
    link2 = '/comic'
    link3 = '/novel'
    link4 = '/story'
    link5 = '/autobiography'
    link6 = '/educational'
    link7 = '/motivational'
    context = {'productss': productss, 'variablemain' : variablemain, 'variable1': variable1, 'variable2': variable2,
    'variable3': variable3, 'variable4': variable4, 'variable5': variable5, 'variable6': variable6, 'variable7': variable7,
    'link1': link1, 'link2': link2, 'link3': link3, 'link4': link4, 'link5': link5, 'link6': link6, 'link7': link7}
    return render(request, 'home.html', context)

def comic(request):
    productss = reversed(Product.objects.all().filter(category = 'Comic'))
    variablemain = 'List of all Comic books availble currently:'
    variable1 = 'Comics'
    variable2 = 'All'
    variable3 = 'Novel'
    variable4 = 'Story'
    variable5 = 'Autobiography'
    variable6 = 'Educational'
    variable7 = 'Motiational'
    link1 = '/comic'
    link2 = '/all'
    link3 = '/novel'
    link4 = '/story'
    link5 = '/autobiography'
    link6 = '/educational'
    link7 = '/motivational'
    context = {'productss': productss, 'variablemain' : variablemain, 'variable1': variable1, 'variable2': variable2,
    'variable3': variable3, 'variable4': variable4, 'variable5': variable5, 'variable6': variable6, 'variable7': variable7,
    'link1': link1, 'link2': link2, 'link3': link3, 'link4': link4, 'link5': link5, 'link6': link6, 'link7': link7}
    return render(request, 'home.html', context)

def novel(request):
    productss = reversed(Product.objects.all().filter(category = 'Novel'))
    variablemain = 'List of all Novels availble currently:'
    variable1 = 'Novel'
    variable2 = 'All'
    variable3 = 'Comics'
    variable4 = 'Story'
    variable5 = 'Autobiography'
    variable6 = 'Educational'
    variable7 = 'Motiational'
    link1 = '/novel'
    link2 = '/all'
    link3 = '/comic'
    link4 = '/story'
    link5 = '/autobiography'
    link6 = '/educational'
    link7 = '/motivational'
    context = {'productss': productss, 'variablemain' : variablemain, 'variable1': variable1, 'variable2': variable2,
    'variable3': variable3, 'variable4': variable4, 'variable5': variable5, 'variable6': variable6, 'variable7': variable7,
    'link1': link1, 'link2': link2, 'link3': link3, 'link4': link4, 'link5': link5, 'link6': link6, 'link7': link7}
    return render(request, 'home.html', context)

def story(request):
    productss = reversed(Product.objects.all().filter(category = 'Story'))
    variablemain = 'List of all Story books availble currently:'
    variable1 = 'Story'
    variable2 = 'All'
    variable3 = 'Comics'
    variable4 = 'Novel'
    variable5 = 'Autobiography'
    variable6 = 'Educational'
    variable7 = 'Motiational'
    link1 = '/story'
    link2 = '/all'
    link3 = '/comic'
    link4 = '/novel'
    link5 = '/autobiography'
    link6 = '/educational'
    link7 = '/motivational'
    context = {'productss': productss, 'variablemain' : variablemain, 'variable1': variable1, 'variable2': variable2,
    'variable3': variable3, 'variable4': variable4, 'variable5': variable5, 'variable6': variable6, 'variable7': variable7,
    'link1': link1, 'link2': link2, 'link3': link3, 'link4': link4, 'link5': link5, 'link6': link6, 'link7': link7}
    return render(request, 'home.html', context)

def autobiography(request):
    productss = reversed(Product.objects.all().filter(category = 'Autobiography'))
    variablemain = 'List of Autobiography books availble currently:'
    variable1 = 'Autobiography'
    variable2 = 'All'
    variable3 = 'Comics'
    variable4 = 'Novel'
    variable5 = 'Story'
    variable6 = 'Educational'
    variable7 = 'Motiational'
    link1 = '/autobiography'
    link2 = '/all'
    link3 = '/comic'
    link4 = '/novel'
    link5 = '/story'
    link6 = '/educational'
    link7 = '/motivational'
    context = {'productss': productss, 'variablemain' : variablemain, 'variable1': variable1, 'variable2': variable2,
    'variable3': variable3, 'variable4': variable4, 'variable5': variable5, 'variable6': variable6, 'variable7': variable7,
    'link1': link1, 'link2': link2, 'link3': link3, 'link4': link4, 'link5': link5, 'link6': link6, 'link7': link7}
    return render(request, 'home.html', context)

def educational(request):
    productss = reversed(Product.objects.all().filter(category = 'Educational'))
    variablemain = 'List of all Educational books availble currently:'
    variable1 = 'Educational'
    variable2 = 'All'
    variable3 = 'Comics'
    variable4 = 'Novel'
    variable5 = 'Story'
    variable6 = 'Autobiography'
    variable7 = 'Motiational'
    link1 = '/educational'
    link2 = '/all'
    link3 = '/comic'
    link4 = '/novel'
    link5 = '/story'
    link6 = '/autobiography'
    link7 = '/motivational'
    context = {'productss': productss, 'variablemain' : variablemain, 'variable1': variable1, 'variable2': variable2,
    'variable3': variable3, 'variable4': variable4, 'variable5': variable5, 'variable6': variable6, 'variable7': variable7,
    'link1': link1, 'link2': link2, 'link3': link3, 'link4': link4, 'link5': link5, 'link6': link6, 'link7': link7}
    return render(request, 'home.html', context)

def motivational(request):
    productss = reversed(Product.objects.all().filter(category = 'Motivational'))
    variablemain = 'List of all Motivational books availble currently:'
    variable1 = 'Motiational'
    variable2 = 'All'
    variable3 = 'Comics'
    variable4 = 'Novel'
    variable5 = 'Story'
    variable6 = 'Autobiography'
    variable7 = 'Educational'
    link1 = '/motivational'
    link2 = '/all'
    link3 = '/comic'
    link4 = '/novel'
    link5 = '/story'
    link6 = '/autobiography'
    link7 = '/educational'
    context = {'productss': productss, 'variablemain' : variablemain, 'variable1': variable1, 'variable2': variable2,
    'variable3': variable3, 'variable4': variable4, 'variable5': variable5, 'variable6': variable6, 'variable7': variable7,
    'link1': link1, 'link2': link2, 'link3': link3, 'link4': link4, 'link5': link5, 'link6': link6, 'link7': link7}
    return render(request, 'home.html', context)


def about(request):
    sub = User.objects.all()
    subcount = len(sub)
    book = Product.objects.all()
    bookcount = len(book)
    comic = Product.objects.all().filter(category = 'Comic')
    comiccount = len(comic)
    novel = Product.objects.all().filter(category = 'Novel')
    novelcount = len(novel)
    story = Product.objects.all().filter(category = 'Story')
    storycount = len(story)
    auto = Product.objects.all().filter(category = 'Autobiography')
    autocount = len(auto)
    edu = Product.objects.all().filter(category = 'Educational')
    educount = len(edu)
    mot = Product.objects.all().filter(category = 'Motivational')
    motcount = len(mot)
    context = {
        'subcount' : subcount, 'bookcount': bookcount, 'comiccount': comiccount,
        'novelcount': novelcount, 'storycount':storycount, 'autocount':autocount, 'educount':educount,
         'motcount':motcount }
    
    return render(request,'about.html', context)

def search(request):
    query = request.GET['buscar']
    if len(query)>50:
        productss = Product.objects.none()
    else:
        productssname = Product.objects.all().filter(Product_name__icontains = query)
        productscategory = Product.objects.all().filter(category__icontains = query)
        productsauther = Product.objects.all().filter(auther__icontains = query)
        productss = productssname.union(productscategory).union(productsauther)
    return render(request, 'search.html',{'productss': productss, 'query': query })

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
            return redirect("all")
        else:
            messages.success(request,"No user found please go back and signin again & if new kindly signup first")
            return redirect('index')
    
    return redirect('index')

def signout(request):
        logout(request)
        messages.success(request,"You have succesfully signout")
        return redirect('index')
        