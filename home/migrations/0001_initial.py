# Generated by Django 5.0.2 on 2024-02-25 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Responsible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=4)),
                ('inventar_number', models.IntegerField(blank=True, unique=True)),
                ('processor', models.CharField(blank=True, max_length=70)),
                ('memory', models.CharField(blank=True, max_length=70)),
                ('keyword_mouse', models.CharField(blank=True, max_length=6)),
                ('mac_address', models.CharField(blank=True, max_length=50)),
                ('ip_address', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(default='В сети', max_length=40, null=True)),
                ('category_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='category', to='home.category')),
                ('model_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='home.model')),
                ('responsible_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.responsible')),
            ],
        ),
    ]