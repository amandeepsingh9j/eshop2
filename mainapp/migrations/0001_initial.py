# Generated by Django 4.2.1 on 2024-03-04 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
                ('addressline1', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('addressline2', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('pic1', models.ImageField(upload_to='upload')),
            ],
        ),
        migrations.CreateModel(
            name='Maincategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('stock', models.CharField(blank=True, default='IN Stock', max_length=20, null=True)),
                ('description', models.TextField(blank=True, default='This is the best Product', null=True)),
                ('baseprice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalprice', models.IntegerField()),
                ('pic1', models.ImageField(blank=True, default='', height_field='500px', null=True, upload_to='upload')),
                ('pic2', models.ImageField(blank=True, default='', height_field='500px', null=True, upload_to='upload')),
                ('pic3', models.ImageField(blank=True, default='', height_field='500px', null=True, upload_to='upload')),
                ('pic4', models.ImageField(blank=True, default='', height_field='500px', null=True, upload_to='upload')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.brand')),
                ('maincategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.maincategory')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.subcategory')),
            ],
        ),
    ]
