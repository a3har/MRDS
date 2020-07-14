# Generated by Django 3.0.2 on 2020-03-07 11:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospital_id', models.CharField(max_length=100)),
                ('Firstname', models.CharField(max_length=200)),
                ('Lastname', models.CharField(max_length=200)),
                ('Age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('Address', models.CharField(max_length=500)),
                ('Phone_Number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Document_type', models.CharField(max_length=20)),
                ('Document_image', models.CharField(max_length=1000)),
                ('Hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.User')),
            ],
        ),
    ]