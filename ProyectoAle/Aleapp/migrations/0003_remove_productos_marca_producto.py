# Generated by Django 5.1 on 2024-10-21 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aleapp', '0002_mensajecontacto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='marca_producto',
        ),
    ]
