# Generated by Django 2.2.12 on 2020-04-23 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_control', '0004_stock_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['id'], 'verbose_name': 'Stock', 'verbose_name_plural': 'Stocks'},
        ),
    ]
