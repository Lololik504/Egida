# Generated by Django 3.1.2 on 2020-10-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201001_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='school',
            name='shortname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
