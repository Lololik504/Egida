# Generated by Django 3.1.1 on 2020-09-26 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200926_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingscharacters',
            name='building_constructions',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.buildingconstructions'),
        ),
        migrations.AlterField(
            model_name='buildingscharacters',
            name='temperatures',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.temperatures'),
        ),
    ]
