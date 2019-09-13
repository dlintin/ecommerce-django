# Generated by Django 2.2.4 on 2019-09-10 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barang', '0008_auto_20190903_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_ordered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=1000000, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barang.Produk')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
