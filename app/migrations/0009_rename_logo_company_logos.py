# Generated by Django 3.2 on 2021-04-07 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210406_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='logo',
            new_name='logos',
        ),
    ]