# Generated by Django 3.1.2 on 2020-10-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20201028_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='phone',
            field=models.CharField(default='', max_length=100, verbose_name='Телефон'),
        ),
    ]