# Generated by Django 4.2.3 on 2023-08-20 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockApp', '0019_remove_sale_part_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sparepart',
            name='part_number',
        ),
    ]
