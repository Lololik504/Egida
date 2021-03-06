# Generated by Django 3.1.2 on 2021-01-28 04:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=300, null=True, verbose_name='Улица')),
                ('street_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер дома')),
                ('type', models.CharField(blank=True, choices=[('Отдельно стоящее', 'Free Standing'), ('Встроенное в многоквартирный дом', 'Build Into Apart'), ('Пристроенное к многоквартирному дому', 'Attached To Apart')], default='Отдельно стоящее', max_length=50, null=True, verbose_name='Вид здания')),
                ('purpose', models.CharField(blank=True, max_length=200, null=True, verbose_name='Назначение здания')),
                ('construction_year', models.IntegerField(blank=True, choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2000, null=True, verbose_name='Год постройки здания')),
                ('building_square', models.IntegerField(blank=True, null=True, verbose_name='Площадь здания')),
                ('land_square', models.IntegerField(blank=True, null=True, verbose_name='Площадь земельного участка')),
                ('number_of_storeys', models.IntegerField(blank=True, null=True, verbose_name='Этажность')),
                ('build_height', models.IntegerField(blank=True, null=True, verbose_name='Высота здания')),
                ('occupancy_proj', models.IntegerField(blank=True, null=True, verbose_name='Наполняемость проектная')),
                ('occupancy_fact', models.IntegerField(blank=True, null=True, verbose_name='Наполняемость фактическая')),
                ('arend_square', models.IntegerField(blank=True, null=True, verbose_name='Площадь зданий/помещений, сдаваемых в аренду')),
                ('arend_use_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Вид исспользования')),
                ('unused_square', models.IntegerField(blank=True, null=True, verbose_name='Площадь неиспользуемых зданий/помещений м.кв')),
                ('repair_need_square', models.IntegerField(blank=True, null=True, verbose_name='Площадь, требующая ремонта')),
                ('technical_condition', models.CharField(blank=True, choices=[('Работоспособное', 'Working'), ('Ограниченно-работоспособное', 'Limited Working'), ('Аварийное', 'Emergency')], max_length=50, null=True, verbose_name='Техническое состояние')),
                ('last_repair_year', models.IntegerField(blank=True, choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2000, null=True, verbose_name='Год последнего капитально ремонта')),
            ],
            options={
                'verbose_name': 'Здание',
                'verbose_name_plural': 'Здания',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=30, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(default=None, max_length=30, null=True, verbose_name='Фамилия')),
                ('patronymic', models.CharField(default=None, max_length=30, null=True, verbose_name='Отчество')),
                ('phone', models.CharField(default=None, max_length=30, null=True, verbose_name='Телефон')),
                ('email', models.CharField(default=None, max_length=50, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонал',
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('air_temperature', models.FloatField(null=True, verbose_name='Температура воздуха')),
                ('coolant_forward_temperature', models.FloatField(null=True, verbose_name='Температура подающего трубопровода')),
                ('coolant_backward_temperature', models.FloatField(null=True, verbose_name='Температура обратного трубопровода')),
                ('forward_pressure', models.FloatField(null=True, verbose_name='Давление на подающем трубопроводе')),
                ('backward_pressure', models.FloatField(null=True, verbose_name='Давление на обратном трубопроводе')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.building', verbose_name='Здание')),
            ],
            options={
                'verbose_name': 'Температурный режим',
                'verbose_name_plural': 'Температуры',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('INN', models.CharField(default='', max_length=13, unique=True, verbose_name='ИНН')),
                ('name', models.CharField(default='', max_length=300, verbose_name='Полное название')),
                ('shortname', models.CharField(default='', max_length=100, unique=True, verbose_name='Краткое название')),
                ('phone', models.CharField(default='', max_length=100, verbose_name='Телефон')),
                ('address', models.CharField(default='', max_length=300, verbose_name='Адрес')),
                ('edu_type', models.CharField(default='', max_length=20, verbose_name='Вид образования')),
                ('form_type', models.CharField(default='', max_length=20, verbose_name='Вид организационно-правовой формы')),
                ('district', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.district', verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Школа',
                'verbose_name_plural': 'Школы',
            },
        ),
        migrations.CreateModel(
            name='Requisites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_site', models.CharField(blank=True, max_length=100, null=True, verbose_name='Оффициальный сайт')),
                ('legal_address_street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Юридический адрес (улица)')),
                ('legal_address_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Юридический адрес (номер дома)')),
                ('formation_date', models.DateField(blank=True, default=datetime.date.today, max_length=100, null=True, verbose_name='Дата образования юридического лица')),
                ('district', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.district', verbose_name='Территориальная принадлежность')),
                ('school', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.school', verbose_name='Школа')),
            ],
            options={
                'verbose_name': 'Реквизиты',
                'verbose_name_plural': 'Реквизиты',
            },
        ),
        migrations.AddField(
            model_name='building',
            name='school',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.school', verbose_name='Школа'),
        ),
        migrations.CreateModel(
            name='ZavHoz',
            fields=[
                ('personal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.personal')),
                ('school', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.school')),
            ],
            options={
                'verbose_name': 'Завхоз',
                'verbose_name_plural': 'Завхозы',
            },
            bases=('main.personal',),
        ),
        migrations.CreateModel(
            name='Updater',
            fields=[
                ('personal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.personal')),
                ('school', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.school')),
            ],
            options={
                'verbose_name': 'Ответственный за заполнение',
                'verbose_name_plural': 'Ответственные за заполнение',
            },
            bases=('main.personal',),
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('personal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.personal')),
                ('school', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.school')),
            ],
            options={
                'verbose_name': 'Руководитель',
                'verbose_name_plural': 'Руководители',
            },
            bases=('main.personal',),
        ),
        migrations.CreateModel(
            name='Bookkeeper',
            fields=[
                ('personal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.personal')),
                ('school', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.school')),
            ],
            options={
                'verbose_name': 'Бухгалтер',
                'verbose_name_plural': 'Бухгалтеры',
            },
            bases=('main.personal',),
        ),
    ]
