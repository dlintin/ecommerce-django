from django.shortcuts import render
from .models import Produk, Warna, KategoriBarang
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    barang = Produk.objects.all()
    warna = Warna.objects.all()
    return render (request, 'home.html', {'barang': barang, 'warna': warna})

# class BarangDetailView(DetailView):
#     model = Produk
#     template_name = 'produk-detail.html'
#     context_object_name = 'barang'

def barangs(request, pk):
    barang = Produk.objects.get(id=pk)
    warna = Warna.objects.filter(object_id=pk)
    return render(request, 'product.html', {'barang': barang, 'warna': warna})

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