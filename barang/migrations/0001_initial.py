# Generated by Django 2.2.4 on 2019-08-14 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KategoriBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaproduk', models.CharField(max_length=50)),
                ('harga', models.DecimalField(decimal_places=10, max_digits=1000000)),
                ('stok', models.IntegerField()),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WarnaProduk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idproduk', models.IntegerField()),
                ('namawarna', models.CharField(max_length=50)),
                ('gambar', models.TextField()),
            ],
        ),
    ]
