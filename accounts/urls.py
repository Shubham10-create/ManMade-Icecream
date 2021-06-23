from os import name
from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = "ManMaDe Ice Cream Admin"          #this all three conditions handles our admin pannel website.
admin.site.site_title = "ManMaDe Ice Cream Admin Portal"
admin.site.index_title = "Welcome to ManMaDe Ice Cream"

urlpatterns = [ 
    path("register", views.register, name='register' ),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
]
