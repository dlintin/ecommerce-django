from django.shortcuts import render
from .models import Produk
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    return render (request, 'home.html',{})

def akun(request):
    return render (request, 'account-details.html',{})

def checkouts(request):
    return render (request, 'checkouts.html',{})

def history(request):
    return render (request, 'account-history.html',{})