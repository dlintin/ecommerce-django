import self as self
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from .forms import *
from .models import *
from pembeli.models import *
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request, **kwargs):
    barang = Produk.objects.all()
    warna = Warna.objects.all()
    # carts = Cart.objects.all()
    qty = Cart.objects.count()
    carts = Cart.objects.filter(user=request.user, ordered=False)
    # jumlah = Cart.get_total_item_price(self)
    return render (request, 'home.html', {'barang': barang, 'warna': warna, 'carts':carts, 'qty':qty,})

def barangs(request, pk):
    barang = Produk.objects.get(id=pk)
    warna = Warna.objects.filter(object_id=pk)
    return render(request, 'product.html', {'barang': barang, 'warna': warna})

class Cekot(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        pembeli_form = PembeliForm()
        kurir_form = KurirForm()
        try:
            order = Cart.objects.filter(user=self.request.user, ordered=False)
            total = (Cart.objects
                .filter(user=self.request.user, ordered=False)
                .aggregate(
                total=Sum('quantity', field="item*quantity")
            )['total']
                )

            # return render(self.request, 'keranjang.html', {'order':order, 'total':total})
            return render(self.request, 'checkouts.html',{'order':order, 'total':total, 'pembeli_form': pembeli_form, 'kurir_form': kurir_form})
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")




@login_required
def history(request):
    return render (request, 'account-history.html',{})

def detail(request):
    return render (request, 'produk-detail.html',{})

@login_required
def keranjang(request):
    return render (request, 'keranjang.html',{})


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Cart.objects.filter(user=self.request.user, ordered=False)
            total = (Cart.objects
                .filter(user=self.request.user, ordered=False)
                .aggregate(
                total=Sum('quantity', field="item*quantity")
            )['total']
                )

            return render(self.request, 'keranjang.html', {'order':order, 'total':total})
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")


@login_required
def add_to_cart(request, pk):
    item = Produk.objects.get(id=pk)
    isi = Cart.objects.filter(user_id=request.user,item_id=pk)
    if isi.exists():
        cart_item = Cart.objects.get(
            item_id=pk
        )
        cart_item.quantity +=1
        cart_item.save()
        return redirect("/")
    else:
        item = Produk.objects.get(id=pk)
        cart_itemx, created = Cart.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False
        )
        cart_itemx.save()
        return redirect("/")

