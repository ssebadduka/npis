# Generated by Django 3.2 on 2021-04-22 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210422_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field_enforcement',
            name='name_of_inspector',
            field=models.CharField(max_length=200),
        ),
    ]
