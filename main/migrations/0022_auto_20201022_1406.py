# Generated by Django 3.1.2 on 2020-10-22 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20201022_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='director',
            field=models.OneToOneField(auto_created=True, default=11, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.personal', verbose_name='Директор'),
        ),
    ]