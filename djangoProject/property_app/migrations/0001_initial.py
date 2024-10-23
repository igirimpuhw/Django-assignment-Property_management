# Generated by Django 5.1.2 on 2024-10-21 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('property_type', models.CharField(choices=[('Apartment', 'Apartment'), ('Commercial', 'Commercial'), ('House', 'House')], max_length=100)),
                ('Number_unit', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('Phone_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_number', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('rent', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_app.property')),
            ],
        ),
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('rent_amount', models.IntegerField()),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_app.tenant')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_app.unit')),
            ],
        ),
    ]
