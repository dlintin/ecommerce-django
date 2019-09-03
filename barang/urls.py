from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='barang-home'), 
    path('item_detail/<int:pk>/', views.barangs, name='item-detail'),
    #jika ulr blog/ kosong maka akan memanggil fungsi "def home" dalam views
  
    path('checkouts/', views.checkouts, name='checkouts-home'), 
    
    path('history/', views.history, name='account-history'), 
    
    path('detail/', views.detail, name='barang-detail'),
    
    path('keranjang/', views.keranjang, name='keranjang'),

    path('add_cart/<int:pk>/', views.add_to_cart, name='add-cart'),

    path('cart/', OrderSummaryView.as_view(), name='cart'),

    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   