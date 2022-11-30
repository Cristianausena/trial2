# Generated by Django 4.1.2 on 2022-11-21 05:39

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='log_record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('idnumber', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('timein', models.CharField(max_length=30)),
                ('timeout', models.CharField(max_length=30)),
                ('vehicleid', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='registered_vehicles',
            fields=[
                ('vehicleid', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('idnumber', models.CharField(max_length=30)),
                ('platenumber', models.CharField(max_length=10)),
                ('vehiclemodel', models.CharField(max_length=12)),
                ('imageF', models.ImageField(upload_to='imageF/')),
                ('imageL', models.ImageField(upload_to='imageL/')),
                ('imageR', models.ImageField(upload_to='imageR/')),
                ('imageB', models.ImageField(upload_to='imageB/')),
                ('ORCR', models.ImageField(upload_to='ORCR/')),
                ('status', models.CharField(max_length=20)),
                ('qrcode', models.ImageField(upload_to='qrcode/')),
                ('approved_by', models.CharField(max_length=50)),
                ('date_approved', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('idnumber', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('birthday', models.CharField(max_length=30)),
                ('contactnumber', models.CharField(max_length=11)),
                ('usertype', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]