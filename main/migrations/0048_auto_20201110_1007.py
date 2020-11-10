# Generated by Django 3.1.2 on 2020-11-10 10:07

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_auto_20201110_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='director',
            field=models.OneToOneField(null=True, auto_created=True, default=main.models.Director.default_director, on_delete=django.db.models.deletion.DO_NOTHING, to='main.director'),
        ),
    ]
