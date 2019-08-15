# Generated by Django 2.2.4 on 2019-08-15 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('barang', '0001_initial'),
    ]

    operations = [
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
        migrations.DeleteModel(
            name='WarnaProduk',
        ),
    ]
