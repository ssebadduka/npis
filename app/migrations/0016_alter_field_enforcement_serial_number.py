# Generated by Django 3.2 on 2021-04-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_field_enforcement_name_of_inspector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field_enforcement',
            name='serial_number',
            field=models.CharField(max_length=200),
        ),
    ]
