# Generated by Django 3.1.2 on 2020-10-22 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20201022_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='director',
            field=models.OneToOneField(auto_created=True, default=15, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.personal', verbose_name='Директор'),
        ),
    ]
