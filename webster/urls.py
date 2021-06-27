from django.contrib import admin
from django.urls import path
from webster import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('home1', views.home1, name='home1'),
    path('home2', views.home2, name='home2'),
    path('home3', views.home3, name='home3'),
    path('home4', views.home4, name='home4'),
    path('home5', views.home5, name='home5'),
    path('home6', views.home6, name='home6'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
   
]
