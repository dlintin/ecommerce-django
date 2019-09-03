from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from pembeli.models import *


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#

class PembeliForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['nama_penerima', 'alamat_pengiriman','tlp_penerima']

class KurirForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['kurir_pengiriman', 'pembayaran']



# 1.nama, alamat, hp
# #
# # 2.kurir, metode_pembayaran
# #
# # 3.pesanan