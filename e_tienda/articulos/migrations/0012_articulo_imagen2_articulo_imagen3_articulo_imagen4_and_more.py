# Generated by Django 4.2.1 on 2023-06-07 02:32

import articulos.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0011_alter_articulo_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=articulos.validators.directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'], code='formato_invalido', message='Sólo se permite formato PNG, JPEG, JPG.')], verbose_name='Foto del Artículo 2'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='imagen3',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=articulos.validators.directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'], code='formato_invalido', message='Sólo se permite formato PNG, JPEG, JPG.')], verbose_name='Foto del Artículo 3'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='imagen4',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=articulos.validators.directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'], code='formato_invalido', message='Sólo se permite formato PNG, JPEG, JPG.')], verbose_name='Foto del Artículo 4'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='imagen5',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=articulos.validators.directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'], code='formato_invalido', message='Sólo se permite formato PNG, JPEG, JPG.')], verbose_name='Foto del Artículo 5'),
        ),
    ]
