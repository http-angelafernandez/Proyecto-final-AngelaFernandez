# Generated by Django 5.1.2 on 2024-11-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_datosextra_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosextra',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datosextra',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares/'),
        ),
    ]