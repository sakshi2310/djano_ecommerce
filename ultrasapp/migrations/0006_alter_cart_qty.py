# Generated by Django 5.0 on 2023-12-26 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultrasapp', '0005_users_states'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]