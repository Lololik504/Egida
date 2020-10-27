# Generated by Django 3.1.2 on 2020-10-20 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20201020_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='address',
            field=models.CharField(default=1, max_length=350, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='director',
            name='school',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='main.school', verbose_name='Школа'),
        ),
    ]