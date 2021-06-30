from django.contrib import admin
from django.urls import path
from webster import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.all, name='all'),
    path('profile', views.profile, name='profile'),
    path('comic', views.comic, name='comic'),
    path('novel', views.novel, name='novel'),
    path('story', views.story, name='story'),
    path('autobiography', views.autobiography, name='autobiography'),
    path('educational', views.educational, name='educational'),
    path('motivational', views.motivational, name='motivational'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
   
]
