from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from pembeli.models import *


class PembeliForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['nama_penerima', 'alamat_pengiriman','tlp_penerima']

class KurirForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['kurir_pengiriman', 'pembayaran']




    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # items = models.ManyToManyField(Cart)
    # tanggal_pesan = models.DateTimeField(default=datetime.now, blank=True)
    # ordered = models.BooleanField(default=False)

    # being_delivered = models.BooleanField(default=False)
    # received = models.BooleanField(default=False)