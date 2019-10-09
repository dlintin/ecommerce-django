# Generated by Django 2.2.5 on 2019-10-07 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('pesan', models.TextField(null=True)),
                ('harga', models.DecimalField(decimal_places=0, max_digits=1000000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KategoriBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Kategori',
            },
        ),
        migrations.CreateModel(
            name='Kurir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kurir', models.CharField(max_length=50)),
                ('tarif', models.DecimalField(decimal_places=0, max_digits=1000000)),
            ],
            options={
                'verbose_name_plural': 'Kurir',
            },
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idorder', models.IntegerField()),
                ('statpembayaran', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Warna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_warna', models.CharField(max_length=100, null=True)),
                ('gambar', models.ImageField(upload_to='images')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaproduk', models.CharField(max_length=50)),
                ('harga', models.DecimalField(decimal_places=0, max_digits=1000000)),
                ('stok', models.IntegerField()),
                ('gambar_barang', models.ImageField(null=True, upload_to='images')),
                ('keterangan', models.TextField()),
                ('kategori_produk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='barang.KategoriBarang')),
            ],
            options={
                'verbose_name_plural': 'Produk',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_penerima', models.CharField(max_length=30, null=True)),
                ('total_pembayaran', models.DecimalField(decimal_places=0, max_digits=1000, null=True)),
                ('tanggal_pesan', models.DateTimeField(blank=True)),
                ('ordered', models.BooleanField(default=False)),
                ('alamat_pengiriman', models.TextField(null=True)),
                ('tlp_penerima', models.CharField(max_length=20, null=True)),
                ('pembayaran', models.CharField(choices=[('cod', 'Cash On Delivery'), ('transfer', 'Bank Transfer')], max_length=20, null=True)),
                ('bukti_pembayaran', models.ImageField(null=True, upload_to='images')),
                ('status_pembayaran', models.BooleanField(default=False)),
                ('telah_dikirim', models.BooleanField(default=False)),
                ('telah_diterima', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='barang.Cart')),
                ('kurir_pengiriman', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='barang.Kurir')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barang.Produk'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
