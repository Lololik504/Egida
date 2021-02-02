# Generated by Django 3.1.2 on 2021-02-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210201_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingconstruction',
            name='foundation_status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Состояние фундамента'),
        ),
        migrations.AddField(
            model_name='buildingconstruction',
            name='foundation_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип фундамента'),
        ),
    ]
