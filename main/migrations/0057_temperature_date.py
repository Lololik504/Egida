# Generated by Django 3.1.2 on 2020-12-14 05:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0056_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
    ]
