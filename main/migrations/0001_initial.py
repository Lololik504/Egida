# Generated by Django 3.1.2 on 2020-10-07 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('INN', models.CharField(default='', max_length=13, unique=True)),
                ('name', models.CharField(default='', max_length=250, unique=True)),
                ('shortname', models.CharField(default='', max_length=100, unique=True)),
                ('phone', models.CharField(default='', max_length=100, unique=True)),
                ('adress', models.CharField(default='', max_length=150, unique=True)),
                ('district', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.district')),
            ],
            options={
                'verbose_name': 'Школа',
                'verbose_name_plural': 'Школы',
            },
        ),
        migrations.CreateModel(
            name='Temperatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coolent_temp', models.IntegerField(blank=True, default=15)),
                ('air_temp', models.IntegerField(blank=True, default=15)),
                ('date', models.DateField(auto_now=True)),
                ('school', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.school')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('patronymic', models.CharField(max_length=30)),
                ('school', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='main.school')),
            ],
            options={
                'verbose_name': 'Директор',
                'verbose_name_plural': 'Директоры',
            },
        ),
    ]
