# Generated by Django 5.0 on 2024-01-01 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultrasapp', '0018_alter_billingdetails_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingdetails',
            name='order_notes',
            field=models.CharField(default='', max_length=100),
        ),
    ]
