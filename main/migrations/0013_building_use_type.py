# Generated by Django 3.1.2 on 2020-10-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20201019_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='use_type',
            field=models.CharField(blank=True, choices=[('Отдельно стоящее', 'Free Standing'), ('Встроенное в многоквартирный дом', 'Build Into Apart'), ('Пристроенное к многоквартирному дому', 'Attached To Apart')], max_length=200, null=True, verbose_name='Назначение здания'),
        ),
    ]