# Generated by Django 2.2.4 on 2019-09-11 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0012_auto_20190910_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_ordered',
            name='order',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='barang.Order'),
        ),
    ]
