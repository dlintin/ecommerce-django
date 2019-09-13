from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class KategoriBarang(models.Model):
    kategori = models.CharField(max_length=50)
    def __str__(self):
        return self.kategori
    class Meta:
        verbose_name_plural = "Kategori"

class Produk(models.Model):
    namaproduk = models.CharField(max_length=50)
    harga = models.DecimalField(max_digits=1000000, decimal_places=2)
    stok = models.IntegerField()
    gambar_barang = models.ImageField(upload_to="images", null=True)
    keterangan = models.TextField() 
    kategori_produk = models.ForeignKey(KategoriBarang, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.namaproduk
    class Meta:
        verbose_name_plural = "Produk"
    
class Warna(models.Model):
    nama_warna = models.CharField(max_length=100, null=True)
    gambar = models.ImageField(upload_to="images")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Produk, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    pesan = models.TextField(null=True)
    harga = models.DecimalField(max_digits=1000000, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.item}, by: {self.user} | {self.quantity} item = {self.item.harga}"

    def get_total_item_price(self):
        return self.quantity * self.item.harga

    def get_total(self):
        total = sum(self.quantity * self.item.harga)
        return total

    def get_total(self):
        total = 0
        for order_item in self.item.all():
            subtotal = sum(self.quantity * self.item.harga)
            total += subtotal
        return total


class Kurir(models.Model):
    nama_kurir = models.CharField(max_length=50)
    tarif = models.DecimalField(max_digits=1000000, decimal_places=2)

    def __str__(self):
        return self.nama_kurir

    class Meta:
        verbose_name_plural = "Kurir"


class Pembayaran(models.Model):
    idorder = models.IntegerField()
    statpembayaran = models.CharField(max_length=50)

metode_pembayaran = (
    ('cod','Cash On Delivery'),
    ('transfer', 'Bank Transfer'),
)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nama_penerima = models.CharField(max_length=30, null=True)
    items = models.ManyToManyField(Cart)
    total_pembayaran = models.DecimalField(max_digits=1000, decimal_places=2, null=True)
    tanggal_pesan = models.DateTimeField(blank=True)
    ordered = models.BooleanField(default=False)
    alamat_pengiriman = models.TextField(null=True)
    tlp_penerima = models.CharField(max_length=20, null=True)
    pembayaran = models.CharField(choices=metode_pembayaran, max_length=20, null=True)
    bukti_pembayaran = models.ImageField(upload_to="images", null=True)
    status_pembayaran = models.BooleanField(default=False)
    kurir_pengiriman = models.ForeignKey(Kurir, on_delete=models.CASCADE, null=True)
    telah_dikirim = models.BooleanField(default=False)
    telah_diterima = models.BooleanField(default=False)

    
    def __str__(self):
        return f"Pembayaran: {self.status_pembayaran}, by: {self.nama_penerima}"
