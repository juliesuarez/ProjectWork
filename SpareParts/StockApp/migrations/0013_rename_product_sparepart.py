# Generated by Django 4.2.3 on 2023-08-16 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockApp', '0012_rename_item_name_product_part_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='SparePart',
        ),
    ]
