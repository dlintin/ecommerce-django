from django.db import models

# Create your models here.
class Pembeli(models.Model):
    namapembeli = models.CharField(max_length=50)
    tlp = models.IntegerField()
    email = models.EmailField()
    password = models.TextField()
    
class AlamatPembeli(models.Model):
    idpembeli = models.CharField(max_length=50)
    alamat = models.IntegerField()