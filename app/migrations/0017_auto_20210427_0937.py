# Generated by Django 3.2 on 2021-04-27 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_field_enforcement_serial_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('attachment_file', models.FileField(upload_to='attachments')),
            ],
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('female', models.PositiveIntegerField(max_length=200)),
                ('male', models.PositiveIntegerField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('partcular', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('remarks', models.TextField(null=True)),
                ('other_details', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('construction_permit', models.CharField(max_length=200, verbose_name='Construction Permit Number')),
                ('operation_permit', models.CharField(max_length=200, verbose_name='Operating License Number')),
                ('TIN', models.CharField(max_length=200, verbose_name='Company Tax identification Number')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_type', models.CharField(choices=[('PMS', 'PMS'), ('AGO', 'AGO'), ('BIK', 'BIK'), ('LPG', 'LPG'), ('OTHERS', 'OTHERS')], max_length=200)),
                ('tank_dtails', models.CharField(max_length=200)),
                ('stock', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Supplers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee_number',
        ),
        migrations.RemoveField(
            model_name='field_inspection',
            name='company',
        ),
        migrations.DeleteModel(
            name='Gps',
        ),
        migrations.DeleteModel(
            name='Permit',
        ),
        migrations.DeleteModel(
            name='Petro_product',
        ),
        migrations.AddField(
            model_name='company',
            name='distance',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='waste',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nemacertifcate',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.DeleteModel(
            name='Field_inspection',
        ),
        migrations.AddField(
            model_name='supplers',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AddField(
            model_name='products',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AddField(
            model_name='permits',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AddField(
            model_name='employees',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AddField(
            model_name='branches',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AddField(
            model_name='attachments',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
    ]