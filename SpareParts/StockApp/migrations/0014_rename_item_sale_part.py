# Generated by Django 4.2.3 on 2023-08-16 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockApp', '0013_rename_product_sparepart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='item',
            new_name='part',
        ),
    ]
