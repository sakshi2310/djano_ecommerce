# Generated by Django 5.0 on 2023-12-27 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ultrasapp', '0006_alter_cart_qty'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
