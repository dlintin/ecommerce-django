from django.shortcuts import render
from .models import Produk, Warna, KategoriBarang
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    barang = Produk.objects.all()
    warna = Warna.objects.all()
    return render (request, 'home.html', {'barang': barang, 'warna': warna})

def barangs(request, pk):
    barang = Produk.objects.get(id=pk)
    warna = Warna.objects.filter(object_id=pk)
    return render(request, 'product.html', {'barang': barang, 'warna': warna})

def checkouts(request):
    return render (request, 'checkouts.html',{})

@login_required
def history(request):
    return render (request, 'account-history.html',{})

def detail(request):
    return render (request, 'produk-detail.html',{})

@login_required
def keranjang(request):
    return render (request, 'keranjang.html',{})


