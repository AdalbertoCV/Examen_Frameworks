# Generated by Django 4.1.6 on 2023-05-05 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_administrador_avatar_remove_cliente_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]