
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import *
from django.views import View
from .models import *
from pembeli.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.db.models import Sum, F, FloatField


def home(request, **kwargs):
    barang = Produk.objects.all()
    warna = Warna.objects.all()
    # carts = Cart.objects.all()
    if request.user.is_authenticated:
        qty = Cart.objects.filter(user=request.user, ordered=False).count()
        carts = Cart.objects.filter(user=request.user, ordered=False)
    # jumlah = Cart.get_total_item_price(self)
        return render (request, 'home.html', {'barang': barang, 'warna': warna, 'carts':carts, 'qty':qty,})
    else:
        return render(request, 'home.html', {'barang': barang, 'warna': warna, })


def barangs(request, pk):
    barang = Produk.objects.get(id=pk)
    warna = Warna.objects.filter(object_id=pk)
    return render(request, 'product.html', {'barang': barang, 'warna': warna})


class checkout(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = Profile.objects.values_list('nama_lengkap', flat=True).get(user_id=self.request.user.id)
        alamat = Profile.objects.values_list('alamat', flat=True).get(user_id=self.request.user.id)
        tlp = Profile.objects.values_list('tlp', flat=True).get(user_id=self.request.user.id)

        #membarikan nilai awal ke form
        pembeli_form = PembeliForm(initial={'nama_penerima': user, 'alamat_pengiriman': alamat, 'tlp_penerima': tlp})
        kurir_form = KurirForm()

        try:
            order = Cart.objects.filter(user=self.request.user, ordered=False)
            total = Cart.objects.filter(user=self.request.user, ordered=False).aggregate(
                total=Sum(F('quantity') * F('harga'), output_field=FloatField()))['total']
            return render(self.request, 'checkouts.html',
                          {'order': order, 'total': total, 'pembeli_form': pembeli_form, 'kurir_form': kurir_form})
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")

def ke_bayar(request,id):
    pembayaran_form = PembayaranForm(request.POST, request.FILES)
    if request.method == 'POST':
        p_form = PembeliForm(request.POST)
        k_form = KurirForm(request.POST)
        if p_form.is_valid() and k_form.is_valid():

            isix = Order.objects.filter(user_id=request.user, ordered=False)
            isi = isix[0]
            if isix.exists():
                isi.nama_penerima = p_form.cleaned_data['nama_penerima']
                isi.alamat_pengiriman = p_form.cleaned_data['alamat_pengiriman']
                isi.tlp_penerima = p_form.cleaned_data['tlp_penerima']
                isi.kurir_pengiriman = k_form.cleaned_data['kurir_pengiriman']
                isi.pembayaran = k_form.cleaned_data['pembayaran']
                isi.save()

                try:
                    total = Cart.objects.filter(user=request.user, ordered=False).aggregate(
                        total=Sum(F('quantity') * F('harga'), output_field=FloatField()))['total']
                except ObjectDoesNotExist:
                    messages.warning(request, "gagal mengambil total pembayaran")

                Cart.objects.filter(user_id = request.user, ordered = False).update(ordered = True)
                bayar = Order.objects.get(user_id=request.user, ordered=False)
                if bayar.pembayaran == 'cod':
                    Order.objects.filter(user_id=request.user, ordered=False).update(ordered=True, total_pembayaran=total)
                    messages.success(request, f'Pesanan selesai dan akan segera Diproses!')
                    return redirect("/")
                else:
                    Order.objects.filter(user_id=request.user, ordered=False).update(ordered=True, total_pembayaran=total)
                    return render(request, 'pembayaran.html',{'total': total, 'pembayaran_form':pembayaran_form,})
            else:

                return redirect("/")


@login_required
def history(request):
    order = Order.objects.filter(ordered = True, user_id = request.user)
    return render (request, 'account-history.html',{'order':order})

def detail(request):
    return render (request, 'produk-detail.html',{})

@login_required
def keranjang(request):
    return render (request, 'keranjang.html',{})


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Cart.objects.filter(user=self.request.user, ordered=False)
            total = Cart.objects.filter(user=self.request.user, ordered=False).aggregate(
                total=Sum(F('quantity') * F('harga'), output_field=FloatField()))['total']

            return render(self.request, 'keranjang.html', {'order':order, 'total':total})
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")



@login_required
def add_to_cart(request, pk):
    item = Produk.objects.get(id=pk)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
        harga=item.harga,
    )
    order_qs = Order.objects.filter(user_id=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("/")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("/")
    else:
        ordered_date = timezone.now()
        orderx = Order.objects.create(user=request.user, tanggal_pesan=ordered_date)
        orderx.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
    return redirect("/")


def bayar_upload(request):
    if request.method == 'POST':
        pembayaran_form = PembayaranForm(request.POST, request.FILES)
        if pembayaran_form.is_valid():
            # instance = Order(file_field=request.FILES['file'])
            x = Order.objects.get(user_id=request.user, ordered=True, pembayaran='transfer', bukti_pembayaran='')
            x.bukti_pembayaran = pembayaran_form.cleaned_data['bukti_pembayaran']
            x.save()
            messages.success(request, f'Pesanan selesai dan akan segera Diproses!')
            return redirect("/")
        else:
            return redirect("/")

