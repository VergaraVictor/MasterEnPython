from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

def about(request):

    return render(request, 'mainapp/about.html', {
        'title': 'Sobre Nosotros'
    })

def register_page(request):

    return render(request, 'users/register.html', {
        'title': 'Registro'
    })