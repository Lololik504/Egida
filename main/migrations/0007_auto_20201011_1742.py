# Generated by Django 3.1.2 on 2020-10-11 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201011_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='adress',
            new_name='address',
        ),
    ]