# Generated by Django 3.1.2 on 2021-01-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0064_auto_20210127_0507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisites',
            name='legal_address',
        ),
        migrations.AddField(
            model_name='requisites',
            name='legal_address_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Юридический адрес (номер дома)'),
        ),
        migrations.AddField(
            model_name='requisites',
            name='legal_address_street',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Юридический адрес (улица)'),
        ),
    ]
