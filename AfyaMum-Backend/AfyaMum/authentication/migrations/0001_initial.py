# Generated by Django 4.2.4 on 2023-08-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('type', models.CharField(choices=[('Mother', 'mother'), ('Specialist', 'specialist')], default='Mother', max_length=10)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('clinic', models.CharField(max_length=30)),
                ('speciality', models.CharField(max_length=30)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('gender', models.CharField(max_length=30)),
                ('residence', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_mother', models.BooleanField(default=False)),
                ('is_specialist', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mother',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authentication.useraccount',),
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authentication.useraccount',),
        ),
    ]
