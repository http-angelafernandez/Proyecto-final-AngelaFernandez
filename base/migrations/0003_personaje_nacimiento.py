# Generated by Django 5.1.2 on 2024-11-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_personaje_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaje',
            name='nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
