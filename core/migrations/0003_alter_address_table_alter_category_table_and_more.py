# Generated by Django 4.0 on 2021-12-12 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_address_apartment_address_address_default_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='address',
            table='address',
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='item',
            table='item',
        ),
        migrations.AlterModelTable(
            name='order',
            table='orders',
        ),
        migrations.AlterModelTable(
            name='orderitems',
            table='order_item',
        ),
        migrations.AlterModelTable(
            name='payment',
            table='payment',
        ),
    ]