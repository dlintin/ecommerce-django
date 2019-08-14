from django.db import models

# Create your models here.
class Produk(models.Model):
    namaproduk = models.CharField(max_length=50)
    harga = models.DecimalField(max_digits=1000000, decimal_places=10)
    stok = models.IntegerField()
    keterangan = models.TextField() 
    
class WarnaProduk(models.Model):
    idproduk = models.IntegerField()
    namawarna = models.CharField(max_length=50)
    gambar = models.TextField()
    
class KategoriBarang(models.Model):
    kategori = models.CharField(max_length=50)
    