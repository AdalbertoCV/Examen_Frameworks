# Generated by Django 4.1.6 on 2023-05-06 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0005_alter_articulo_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='descripcion',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
