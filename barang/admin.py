from django.contrib import admin
from .models import *
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
# admin.site.register(Cart)

admin.site.register(Kurir)
admin.site.register(Order)
