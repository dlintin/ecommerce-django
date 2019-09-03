from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum
from django.shortcuts import reverse



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

    def __str__(self):
        return f"{self.quantity} of {self.item.harga}"

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
#
# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     items = models.ManyToManyField(Cart)
#     start_date = models.DateTimeField(auto_now_add=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)
#     shipping_address = models.ForeignKey(
#         'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
#     payment = models.ForeignKey(
#         'Payment', on_delete=models.SET_NULL, blank=True, null=True)
#     being_delivered = models.BooleanField(default=False)
#     received = models.BooleanField(default=False)


class Kurir(models.Model):
    namakurir = models.CharField(max_length=50)
    hargakilo = models.DecimalField(max_digits=1000000, decimal_places=2)

    def __str__(self):
        return self.namakurir

    class Meta:
        verbose_name_plural = "Kurir"


class Pembayaran(models.Model):
    idorder = models.IntegerField()
    statpembayaran = models.CharField(max_length=50)