# Generated by Django 3.1.2 on 2020-10-07 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='userProfile',
        ),
    ]