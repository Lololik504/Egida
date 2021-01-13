# Generated by Django 3.1.2 on 2021-01-13 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_auto_20210113_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='minimal_temperature',
            field=models.FloatField(null=True, verbose_name='Минимальная температура'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='backward_pressure',
            field=models.FloatField(null=True, verbose_name='Давление на обратном трубопроводе'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='coolant_backward_temperature',
            field=models.FloatField(null=True, verbose_name='Температура обратного трубопровода'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='coolant_forward_temperature',
            field=models.FloatField(null=True, verbose_name='Температура подающего трубопровода'),
        ),
    ]
