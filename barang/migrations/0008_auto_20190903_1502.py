# Generated by Django 2.2.4 on 2019-09-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0007_auto_20190903_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='harga',
            field=models.DecimalField(decimal_places=2, max_digits=1000000, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='nama_penerima',
            field=models.CharField(max_length=30, null=True),
        ),
    ]