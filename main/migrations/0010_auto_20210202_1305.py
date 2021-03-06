# Generated by Django 3.1.2 on 2021-02-02 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210201_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndoorAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_room_total_count', models.IntegerField(blank=True, null=True, verbose_name='Общее количество учебных/игровых помещений')),
                ('admin_room_technical_condition', models.CharField(blank=True, max_length=50, null=True, verbose_name='Техническое состояние учебных помещений')),
                ('admin_room_count_of_technical_condition_field', models.IntegerField(blank=True, null=True, verbose_name='Количество административных помещений, относящихся к полю технического состояния')),
                ('auditorium_technical_condition', models.CharField(blank=True, max_length=50, null=True, verbose_name='Техническое состояние актовых залов')),
                ('auditorium_percent_of_technical_condition_field', models.FloatField(blank=True, null=True, verbose_name='Процент актовых залов, относящихся к полю технического состояния')),
                ('auditorium_exhaust_ventilation', models.BooleanField(blank=True, null=True, verbose_name='Наличие вытяжной вентиляции в актовых залах')),
                ('auditorium_exhaust_ventilation_is_workable', models.BooleanField(blank=True, null=True, verbose_name='Вытяжная вентиляция в актовых залах работоспособна')),
                ('auditorium_ventilation_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип вентиляции в актовых залах')),
                ('auditorium_supply_ventilation', models.BooleanField(blank=True, null=True, verbose_name='Наличие приточной вентиляции в актовых залах')),
                ('auditorium_supply_ventilation_is_workable', models.BooleanField(blank=True, null=True, verbose_name='Приточная вентиляция в актовых залах работоспособна')),
                ('auditorium_air_heater_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип воздухонагревателя в актовых залах')),
                ('bathroom_total_count', models.IntegerField(blank=True, null=True, verbose_name='Общее количество санузлов')),
                ('bathroom_technical_condition', models.CharField(blank=True, max_length=50, null=True, verbose_name='Техническое состояние санузлов')),
                ('bathroom_count_of_technical_condition_field', models.IntegerField(blank=True, null=True, verbose_name='Количество санузлов, относящихся к полю технического состояния')),
                ('bathroom_exhaust_ventilation', models.BooleanField(blank=True, null=True, verbose_name='Наличие вытяжной вентиляции в санузлах')),
                ('bathroom_exhaust_ventilation_is_workable', models.BooleanField(blank=True, null=True, verbose_name='Вытяжная вентиляция в санузлах работоспособна')),
                ('bathroom_ventilation_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип вентиляции в санузлах')),
                ('total_classroom_count', models.IntegerField(blank=True, null=True, verbose_name='Общее количество учебных/игровых помещений')),
                ('classrooms_technical_condition', models.CharField(blank=True, max_length=50, null=True, verbose_name='Техническое состояние учебных помещений')),
                ('classroom_count_of_technical_condition_field', models.IntegerField(blank=True, null=True, verbose_name='Количество учебных/игровых помещений, относящихся к полю технического состояния')),
                ('corridors_technical_condition', models.CharField(blank=True, max_length=50, null=True, verbose_name='Техническое состояние учебных помещений')),
                ('corridors_percent_of_technical_condition_field', models.FloatField(blank=True, null=True, verbose_name='Процент коридоров, относящихся к полю технического состояния')),
                ('emergency_exit_total_count', models.IntegerField(blank=True, null=True, verbose_name='Общее количество эвакуационных выходов')),
                ('emergency_exit_condition', models.CharField(blank=True, max_length=50, null=True, verbose_name='Техническое состояние эвакуационных выходов')),
                ('emergency_exit_count_of_technical_condition_field', models.IntegerField(blank=True, null=True, verbose_name='Количество эвакуационных выходов, относящихся к полю технического состояния')),
                ('auto_opening_of_emergency_exits_system', models.BooleanField(blank=True, null=True, verbose_name='Наличие системы автоматического открывания эвакуационных выходов')),
                ('food_block_technical_condition', models.CharField(blank=True, max_length=50, null=True, verbose_name='Техническое состояние пищеблока')),
                ('food_block_exhaust_ventilation', models.BooleanField(blank=True, null=True, verbose_name='Наличие вытяжной вентиляции в пищеблоке')),
                ('food_block_exhaust_ventilation_is_workable', models.BooleanField(blank=True, null=True, verbose_name='Вытяжная вентиляция в пищеблоке работоспособна')),
                ('food_block_ventilation_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип вентиляции в пищеблоке')),
                ('food_block_supply_ventilation', models.BooleanField(blank=True, null=True, verbose_name='Наличие приточной вентиляции в пищеблоке')),
                ('food_block_supply_ventilation_is_workable', models.BooleanField(blank=True, null=True, verbose_name='Приточная вентиляция в пищеблоке работоспособна')),
                ('food_block_air_heater_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип воздухонагревателя в пищеблоке')),
                ('gym_room_total_count', models.IntegerField(blank=True, null=True, verbose_name='Общее количество спортзалов')),
                ('gym_technical_condition', models.CharField(blank=True, max_length=50, null=True, verbose_name='Техническое состояние спортзалов')),
                ('gym_percent_of_technical_condition_field', models.FloatField(blank=True, null=True, verbose_name='Процент спортзалов, относящихся к полю технического состояния')),
                ('gym_exhaust_ventilation', models.BooleanField(blank=True, null=True, verbose_name='Наличие вытяжной вентиляции в спортзалах')),
                ('gym_exhaust_ventilation_is_workable', models.BooleanField(blank=True, null=True, verbose_name='Вытяжная вентиляция в спортзалах работоспособна')),
                ('gym_ventilation_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип вентиляции в спортзалах')),
                ('gym_supply_ventilation', models.BooleanField(blank=True, null=True, verbose_name='Наличие приточной вентиляции в спортзалах')),
                ('gym_supply_ventilation_is_workable', models.BooleanField(blank=True, null=True, verbose_name='Приточная вентиляция в спортзалах работоспособна')),
                ('gym_air_heater_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип воздухонагревателя в спортзалах')),
                ('laundry_technical_condition', models.CharField(blank=True, max_length=50, null=True, verbose_name='Техническое состояние прачечной')),
                ('laundry_exhaust_ventilation', models.BooleanField(blank=True, null=True, verbose_name='Наличие вытяжной вентиляции в прачечной')),
                ('laundry_exhaust_ventilation_is_workable', models.BooleanField(blank=True, null=True, verbose_name='Вытяжная вентиляция в прачечной работоспособна')),
                ('laundry_ventilation_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип вентиляции в прачечной')),
                ('pantry_total_count', models.IntegerField(blank=True, null=True, verbose_name='Общее количество буфетных')),
                ('pantry_technical_condition', models.CharField(blank=True, max_length=50, null=True, verbose_name='Техническое состояние буфетных')),
                ('pantry_count_of_technical_condition_field', models.IntegerField(blank=True, null=True, verbose_name='Количество буфетных, относящихся к полю технического состояния')),
            ],
            options={
                'verbose_name': 'Внутренние помещения',
            },
        ),
        migrations.AlterField(
            model_name='engineeringcommunication',
            name='storm_water_inlet',
            field=models.BooleanField(blank=True, null=True, verbose_name='Наличие дождеприемника на территории учреждения'),
        ),
        migrations.AlterField(
            model_name='engineeringcommunication',
            name='thermal_loads_heating',
            field=models.IntegerField(blank=True, null=True, verbose_name='Тепловая нагрузка (Отопление)'),
        ),
        migrations.AlterField(
            model_name='engineeringcommunication',
            name='thermal_loads_hot_water_supply',
            field=models.IntegerField(blank=True, null=True, verbose_name='Тепловая нагрузка (Горячее водоснабжение)'),
        ),
        migrations.AlterField(
            model_name='engineeringcommunication',
            name='thermal_loads_total',
            field=models.IntegerField(blank=True, null=True, verbose_name='Тепловая нагрузка (Суммарная)'),
        ),
        migrations.AlterField(
            model_name='engineeringcommunication',
            name='thermal_loads_ventilation',
            field=models.IntegerField(blank=True, null=True, verbose_name='Тепловая нагрузка (Вентиляция)'),
        ),
    ]
