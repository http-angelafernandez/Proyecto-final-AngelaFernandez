# Generated by Django 5.1.2 on 2024-11-02 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_datosextra_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosextra',
            name='descripcion',
        ),
    ]