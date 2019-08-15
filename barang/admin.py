from django.contrib import admin
from .models import Produk, Warna, KategoriBarang
from django.contrib.contenttypes.admin import GenericTabularInline



# Register your models here.
class ImageInline(GenericTabularInline):
    model = Warna

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    
admin.site.register(Produk, ProductAdmin)
admin.site.register(KategoriBarang)