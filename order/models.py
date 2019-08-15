from django.db import models

# Create your models here.
class Keranjang(models.Model):
    idPembeli = models.IntegerField()
    idBarang = models.IntegerField()
    jumlahKeranjang = models.IntegerField()
    alamatKirim = models.CharField(max_length=50)
    berat = models.IntegerField()
    totalharga = models.DecimalField(max_digits=1000000, decimal_places=2)
    
class Kurir(models.Model):
    namakurir = models.CharField(max_length=50)
    hargakilo = models.DecimalField(max_digits=1000000, decimal_places=2)
    
class Order(models.Model):
    idorder = models.IntegerField()
    idbarang = models.IntegerField()
    jumlahOrder = models.IntegerField()
    ongkir = models.DecimalField(max_digits=1000000, decimal_places=2)
    
class Pembayaran(models.Model):
    idorder = models.IntegerField()
    statpembayaran = models.CharField(max_length=50)
    
    