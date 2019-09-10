from django.db import models
# Create your models here.
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from barang.models import *


class Product(models.Model):
    nana_produk = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.nana_produk

class Image(models.Model):
    namex = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="images")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

class Orderiaaa(models.Model):
    nama_penerima = models.CharField(max_length=30, null=True)
    item_pesan = models.ManyToManyField(Cart)

    def __str__(self):
        return f"{self.item_pesan.all()}, by: {self.nama_penerima}"