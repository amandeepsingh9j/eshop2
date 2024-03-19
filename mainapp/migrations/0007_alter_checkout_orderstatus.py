# Generated by Django 4.2.1 on 2024-03-13 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_checkout_orderstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='orderstatus',
            field=models.IntegerField(choices=[(0, 'Order Placed'), (1, 'Not Packed'), (2, 'Packed'), (3, 'Ready To Ship'), (4, 'Shipped'), (5, 'Out for Delivery'), (6, 'Delivery'), (7, 'Cancelled')], default=0),
        ),
    ]
