# Generated by Django 4.2.1 on 2024-03-13 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_rename_name_wishlist_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('shipping', models.IntegerField()),
                ('final', models.IntegerField()),
                ('rppid', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('paymentmode', models.IntegerField(choices=[(0, 'COD'), (1, 'Net Banking')], default=0)),
                ('paymentstatus', models.IntegerField(choices=[(0, 'Pending'), (1, 'Done')], default=0)),
                ('orderstatus', models.IntegerField(choices=[(0, 'Order Placed'), (1, 'Not Packed'), (2, 'Packed'), (3, 'Ready To Ship'), (4, 'Shipped'), (5, 'Out for Delivery'), (6, 'Delivery'), (7, 'Cancelled')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.buyer')),
            ],
        ),
        migrations.CreateModel(
            name='Checkoutproduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.checkout')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
            ],
        ),
    ]
