from os import name
from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "ManMaDe Ice Cream Admin"          #this all three conditions handles our admin pannel website.
admin.site.site_title = "ManMaDe Ice Cream Admin Portal"
admin.site.index_title = "Welcome to ManMaDe Ice Cream"

urlpatterns = [ 
    path("", views.index, name='home'), #it runs the index function in views 
                                        #it tells that if any blank request comes,it goes to home page
    path("about", views.about, name='about'),
    path("kulfi", views.kulfi, name='kulfi'),
    path("falooda", views.falooda, name='falooda'),
    path("rolled", views.rolled, name='rolled'),
    path("popsicle", views.popsicle, name='popsicle'),
    path("familypack", views.familypack, name='familypack'),
    path("gelato", views.gelato, name='gelato'),
    path("contact", views.contact, name='contact'),
]
