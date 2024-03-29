# Generated by Django 5.0 on 2023-12-27 22:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultras_adminapp', '0017_multipleproimage'),
        ('ultrasapp', '0014_rename_procut_id_cart_prodcut_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_status', models.CharField(max_length=100)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultras_adminapp.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultrasapp.users')),
            ],
        ),
    ]
