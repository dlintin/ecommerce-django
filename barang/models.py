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
    