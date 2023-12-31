# Generated by Django 4.2.3 on 2023-08-01 06:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('StockApp', '0003_product_branch_name_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_of_arrival',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='sales',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
