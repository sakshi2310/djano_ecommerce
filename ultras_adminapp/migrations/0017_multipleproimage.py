# Generated by Django 5.0 on 2023-12-25 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultras_adminapp', '0016_delete_multipleproimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleProImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='', upload_to='media/')),
                ('product_id', models.IntegerField()),
            ],
        ),
    ]
