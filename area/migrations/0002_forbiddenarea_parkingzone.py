# Generated by Django 3.2.9 on 2021-11-20 15:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForbiddenArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boundary', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('coords', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
            options={
                'db_table': 'forbidden_areas',
            },
        ),
        migrations.CreateModel(
            name='Parkingzone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_lat', models.DecimalField(decimal_places=14, max_digits=17)),
                ('center_lng', models.DecimalField(decimal_places=14, max_digits=17)),
                ('radius', models.FloatField()),
            ],
            options={
                'db_table': 'parkingzones',
            },
        ),
    ]
