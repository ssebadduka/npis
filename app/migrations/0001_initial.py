# Generated by Django 3.2 on 2021-05-19 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('facility_type', models.CharField(choices=[('Depot', 'Depot'), ('Truck', 'Truck'), ('Service', 'Service'), ('Filling Station', 'Filling Station')], max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=150)),
                ('registration_no', models.CharField(max_length=50)),
                ('contact_person', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('sub_county', models.CharField(max_length=50)),
                ('post_code', models.CharField(max_length=50)),
                ('village', models.CharField(max_length=50)),
                ('ownership', models.CharField(max_length=50)),
                ('parish', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
                ('tin', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=None)),
                ('distance', models.CharField(max_length=100, null=True, verbose_name='Distance from Nearest Licensed Station.')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companys',
            },
        ),
        migrations.CreateModel(
            name='CompanyInspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspection_no', models.CharField(max_length=25)),
                ('inspection_date', models.DateField()),
                ('inspector', models.CharField(max_length=50, verbose_name='Inspected By')),
                ('recommendation', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Field_enforcement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default='2021-05-12')),
                ('company_name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('seal_number_placed_on_nozzle', models.CharField(max_length=200)),
                ('serial_number', models.CharField(max_length=200, unique=True)),
                ('contact', models.CharField(max_length=200)),
                ('truck_number', models.CharField(blank=True, max_length=200, null=True)),
                ('subcounty', models.CharField(max_length=200, verbose_name='Subcounty/Divison/Municipality')),
                ('seal_placed_on', models.CharField(blank=True, max_length=200, null=True, verbose_name='Seal Number(s) placed on underground tanks ')),
                ('illegal_operation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation of petroleum facility')),
                ('illegal_construction', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal construction of petroleum facility')),
                ('Adulteraon_fuel', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Adulteraon of fuel')),
                ('continuous_operation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous operation without carrying out annual EIA audit')),
                ('illegal_operation_business', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and construction in front of congested business premises ')),
                ('illegal_operation_power_line', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and construction under high voltage power transmission line  ')),
                ('illegal_operation_dangerous_corner', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and construction in a dangerous corner  ')),
                ('illegal_operation_reserve_area', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and construction in a road reserve area  ')),
                ('illegal_operation_bypassing_seals', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation aer breaking and/ or bypassing seals  ')),
                ('already', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Already has knowledge of requirement to obtain POL & PCP  ')),
                ('facility_standards', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and construction which does not meet petroleum facility standards  ')),
                ('Social_aspects', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Social aspects involving facility ')),
                ('facility_operator', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Misrepresentaon of branding by facility operator ')),
                ('Impersonaon', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name="Impersonaon by using another's license / permit  ")),
                ('displaying_license', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and /or construction without displaying license /permit from MEMD  ')),
                ('uganda_police', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation aer having been reported to uganda police  ')),
                ('land_plot_size', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and construction on inadequate land plot size (show size )')),
                ('under_reference', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and / or construction reported to uganda police under reference')),
                ('inadequate_size_land', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, verbose_name='Continuous illegal operation and / or construction using a POL and PCP respecvely on an inadequate size of land')),
                ('others', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200)),
                ('remarks', models.TextField(max_length=200)),
                ('name_of_inspector', models.CharField(max_length=200)),
                ('Name_Dealer', models.CharField(max_length=200, verbose_name='Name of Dealer / Representave')),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='SampleRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reg_no', models.CharField(max_length=50, unique=True, verbose_name='Request No.')),
                ('registration_date', models.DateField(null=True)),
                ('representative', models.CharField(max_length=50)),
                ('report_date', models.CharField(max_length=50, verbose_name='Expected Report Date')),
                ('remarks', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
            options={
                'verbose_name': 'SampleRequest',
                'verbose_name_plural': 'SampleRequests',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_type', models.CharField(choices=[('PMS', 'PMS'), ('AGO', 'AGO'), ('BIK', 'BIK'), ('OTHERS', 'OTHERS')], max_length=200)),
                ('tank_details', models.CharField(max_length=200)),
                ('stock', models.CharField(max_length=200)),
                ('product_prices', models.CharField(max_length=150)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_prices', models.CharField(max_length=150)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.products')),
            ],
        ),
        migrations.CreateModel(
            name='Permits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('construction_permit', models.CharField(max_length=200, verbose_name='Construction Permit Number')),
                ('operation_permit', models.CharField(max_length=200, verbose_name='Operating License Number')),
                ('TIN', models.CharField(max_length=200, verbose_name='Company Tax identification Number')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='NemaCertifcate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('certificate_no', models.CharField(max_length=25, verbose_name='NEMA Certificate No.')),
                ('create_date', models.DateField()),
                ('audit_due_date', models.DateField()),
                ('project', models.CharField(max_length=50)),
                ('project_purpose', models.TextField()),
                ('received_date', models.DateField()),
                ('certifcate_one', models.FileField(upload_to='')),
                ('certifcate_two', models.FileField(upload_to='')),
                ('certifcate_three', models.FileField(upload_to='')),
                ('status', models.CharField(max_length=100)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='InspectionCheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('remarks', models.TextField()),
                ('checkList', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.checklist', verbose_name='Particular')),
                ('company_inspection', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.companyinspection')),
            ],
        ),
        migrations.CreateModel(
            name='Gas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LPG_prices', models.PositiveIntegerField()),
                ('LPG_item', models.CharField(max_length=150)),
                ('LPG_Description', models.CharField(max_length=150)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('female', models.PositiveIntegerField()),
                ('male', models.PositiveIntegerField()),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('attachment_file', models.FileField(upload_to='attachments')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fuel_type', models.CharField(choices=[('PMS(Gasoline)', 'PMS(Gasoline)'), ('DS', 'AGO(Diesel)'), ('KS', 'BIK(Keresone)'), ('EO', 'Engine Oil'), ('JF', 'Jet Fuel'), ('FO', 'Furnance Oil')], max_length=50)),
                ('parameter', models.CharField(choices=[('Mk', 'Marker'), ('DS', 'Density'), ('Qu', 'Quality')], max_length=20)),
                ('type_method', models.CharField(max_length=10)),
                ('test_method', models.CharField(max_length=10)),
                ('unit_fee', models.IntegerField()),
                ('quantity', models.IntegerField(verbose_name='Quantity(mls)')),
                ('sample_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.samplerequest')),
            ],
            options={
                'verbose_name': 'Sample',
                'verbose_name_plural': 'Samples',
                'unique_together': {('sample_request', 'fuel_type')},
            },
        ),
    ]
