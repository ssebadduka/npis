# Generated by Django 3.2 on 2021-04-22 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_employee_number_field_enforcement_field_inspection_gps_permit_petro_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field_enforcement',
            name='Adulteraon_fuel',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Adulteraon of fuel'),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='Impersonaon',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name="Impersonaon by using another's license / permit  "),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='Social_aspects',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Social aspects involving facility '),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='already',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Already has knowledge of requirement to obtain POL & PCP  '),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='contact',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='continuous_operation',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous operation without carrying out annual EIA audit'),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='displaying_license',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and /or construction without displaying license /permit from MEMD  '),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='facility_operator',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Misrepresentaon of branding by facility operator '),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='facility_standards',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and construction which does not meet petroleum facility standards  '),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='illegal_construction',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal construction of petroleum facility'),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='illegal_operation',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation of petroleum facility'),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='illegal_operation_business',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and construction in front of congested business premises '),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='illegal_operation_bypassing_seals',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation aer breaking and/ or bypassing seals  '),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='illegal_operation_dangerous_corner',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and construction in a dangerous corner  '),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='illegal_operation_power_line',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and construction under high voltage power transmission line  '),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='illegal_operation_reserve_area',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and construction in a road reserve area  '),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='inadequate_size_land',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and / or construction using a POL and PCP respecvely on an inadequate size of land'),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='land_plot_size',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and construction on inadequate land plot size (show size )'),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='others',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='serial_number',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='uganda_police',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation aer having been reported to uganda police  '),
        ),
        migrations.AlterField(
            model_name='field_enforcement',
            name='under_reference',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and / or construction reported to uganda police under reference'),
        ),
    ]
