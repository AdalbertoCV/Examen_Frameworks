# Generated by Django 4.1.6 on 2023-05-04 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('talla', models.CharField(choices=[('', 'Unitalla'), ('1', 'CH'), ('2', 'M'), ('3', 'G'), ('4', 'XL')], max_length=8)),
                ('descripcion', models.CharField(max_length=250)),
                ('imagen', models.ImageField(upload_to='articulos', verbose_name='Foto del Artículo')),
            ],
        ),
    ]
