# Generated by Django 5.1 on 2024-08-16 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_rename_measurement_data_measurement_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='id_sensor',
            new_name='sensor',
        ),
    ]
