from django.db import models

# Create your models here.
class Pembeli(models.Model):
    namapembeli = models.CharField(max_length=50)
    tlp = models.IntegerField()
    email = models.EmailField()
    password = models.TextField()
    def __str__(self):
        return self.namapembeli
    class Meta:
        verbose_name_plural = "Pembeli"
    
class AlamatPembeli(models.Model):
    idpembeli = models.CharField(max_length=50)
    alamat = models.IntegerField()
    def __str__(self):
        return self.alamat
    class Meta:
        verbose_name_plural = "Alamat"