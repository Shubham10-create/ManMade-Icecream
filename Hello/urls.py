"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#first the requested url will come here, and from here it will be sent to any app.py url 
#This whole process is known as url dispatcher
#Any url we enter it goes to home first, if it matches to home it goes wherever its described to go 

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "ManMade Ice Cream Admin"
admin.site.site_title = "ManMade Ice Cream Admin Portal"
admin.site.index_title = "Welcome to ManMade Ice Cream Researcher Portal"

urlpatterns = [ 
    path('admin/', admin.site.urls), #this line basically says whomsoever writes admin/ send them to admins page
    path('',include('home.urls')), #send him to home page, '' - represents blank path
    path('accounts/',include('accounts.urls'))
]
