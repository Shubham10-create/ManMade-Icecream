from home.models import Contact
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
#render function renders the template


# Create your views here.
def index(request):
    return render(request, 'index.html')  #basically renders the template index.html

def about(request):
    return render(request, 'about.html')

def kulfi(request):
    return render(request, 'kulfi.html')

def falooda(request):
    return render(request, 'falooda.html')

def rolled(request):
    return render(request, 'rolled.html')

def popsicle(request):
    return render(request, 'popsicle.html')

def familypack(request):
    return render(request, 'familypack.html')

def gelato(request):
    return render(request, 'gelato.html')
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name') #.get is a method we applied on request.POST
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc) #making contact object
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
    

