from django.shortcuts import render
from .models import Produk
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    barang = {
        'barang': Produk.objects.all()
    }
    return render (request, 'home.html',barang)

def akun(request):
    return render (request, 'account-details.html',{})

def checkouts(request):
    return render (request, 'checkouts.html',{})

def history(request):
    return render (request, 'account-history.html',{})

def detail(request):
    return render (request, 'produk-detail.html',{})

def login(request):
    return render (request, 'login.html',{})

def register(request):
    return render (request, 'register.html',{})

def keranjang(request):
    return render (request, 'keranjang.html',{})