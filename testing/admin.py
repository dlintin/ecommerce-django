from django.contrib import admin
from .models import *
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.
class ImageInline(GenericTabularInline):
    model = Image

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

# admin.site.register(Product, ProductAdmin)
# admin.site.register(Orderiaaa)
# admin.site.register(Alat)