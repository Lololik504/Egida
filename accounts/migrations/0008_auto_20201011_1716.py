# Generated by Django 3.1.2 on 2020-10-11 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_adminuser_departamentuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='permission',
            field=models.IntegerField(choices=[(1, 'Admin'), (5, 'Departament'), (10, 'District'), (15, 'School')]),
        ),
    ]
