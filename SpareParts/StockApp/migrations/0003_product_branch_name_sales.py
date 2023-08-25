# Generated by Django 4.2.3 on 2023-08-01 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StockApp', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='branch_name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('amount_received', models.IntegerField(default=0)),
                ('issued_to', models.CharField(max_length=100)),
                ('unit_price', models.IntegerField(default=0)),
                ('branch_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StockApp.product')),
            ],
        ),
    ]