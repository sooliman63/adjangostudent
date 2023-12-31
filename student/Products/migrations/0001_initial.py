# Generated by Django 4.2.3 on 2023-08-01 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('profile', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='seller/photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='product/photos/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Products.seller')),
            ],
        ),
    ]
