from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='barang-home'), 
    path('item_detail/<int:pk>/', views.barangs, name='item-detail'),
    #jika ulr blog/ kosong maka akan memanggil fungsi "def home" dalam views
    path('akun/', views.akun, name='akun-home'), 
    
    path('checkouts/', views.checkouts, name='checkouts-home'), 
    
    path('history/', views.history, name='account-history'), 
    
    path('detail/', views.detail, name='barang-detail'), 
    
    path('login/', views.login, name='login'), 
    
    path('register/', views.register, name='register'), 
    
    path('keranjang/', views.keranjang, name='keranjang'), 
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   