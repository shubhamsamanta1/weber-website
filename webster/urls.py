from django.contrib import admin
from django.urls import path
from webster import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('error', views.error, name='error'),
    path('success', views.success, name='success'),
    path('logerror', views.logerror, name='logerror'),
    path('usermatch', views.usermatch, name='usermatch'),
    path('mailmatch', views.mailmatch, name='mailmatch'),
]
