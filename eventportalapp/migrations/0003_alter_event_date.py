# Generated by Django 5.0.3 on 2024-03-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventportalapp', '0002_remove_event_reg_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
    ]
