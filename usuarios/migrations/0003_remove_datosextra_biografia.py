# Generated by Django 5.1.2 on 2024-11-02 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_datosextra_biografia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosextra',
            name='biografia',
        ),
    ]
