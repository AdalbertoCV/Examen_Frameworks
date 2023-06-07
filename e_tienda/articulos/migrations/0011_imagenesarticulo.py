# Generated by Django 4.1.6 on 2023-06-03 02:09

import articulos.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0010_alter_articulo_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesArticulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_articulo', models.ImageField(upload_to=articulos.validators.directory_path)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulos.articulo')),
            ],
        ),
    ]
