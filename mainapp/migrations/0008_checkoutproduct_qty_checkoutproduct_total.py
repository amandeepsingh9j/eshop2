# Generated by Django 4.2.1 on 2024-03-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_checkout_orderstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutproduct',
            name='qty',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='checkoutproduct',
            name='total',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
