# Generated by Django 2.2.4 on 2019-08-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keranjang',
            name='totalharga',
            field=models.DecimalField(decimal_places=2, max_digits=1000000),
        ),
        migrations.AlterField(
            model_name='kurir',
            name='hargakilo',
            field=models.DecimalField(decimal_places=2, max_digits=1000000),
        ),
        migrations.AlterField(
            model_name='order',
            name='ongkir',
            field=models.DecimalField(decimal_places=2, max_digits=1000000),
        ),
    ]
