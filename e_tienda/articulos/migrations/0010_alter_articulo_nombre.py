# Generated by Django 4.1.4 on 2023-05-18 20:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0009_resena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='nombre',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('[+-/%]', inverse_match=True)]),
        ),
    ]
