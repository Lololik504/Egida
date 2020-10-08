# Generated by Django 3.1.2 on 2020-10-08 11:39

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201008_0217'),
        ('accounts', '0004_auto_20201008_0322'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='schooluser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DistrictUser',
            fields=[
                ('myuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.myuser')),
                ('district', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.district')),
            ],
            options={
                'verbose_name': 'Пользователь района',
                'verbose_name_plural': 'Пользователи района',
            },
            bases=('accounts.myuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
