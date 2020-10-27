import xlrd
import xlwt
import json
from loguru import logger
from rest_framework.parsers import JSONParser
from xlwt import Worksheet

from Egida import settings
from accounts.models import SchoolUser
from main.models import *

START_ROW = 4
START_COLUMN = 1


def create_new_schools_and_users_from_excel(file_path):
    dir = file_path
    rb = xlrd.open_workbook(dir)
    sheet = rb.sheet_by_index(0)
    for i in range(4, sheet.nrows):
        done = int(float(i) / float(sheet.nrows) * 100)
        logger.info(str.format("IMPORT DONE ON {0}%", done))
        values = sheet.row_values(i)
        INN = int(values[0])
        district = values[1]
        name = values[2]
        shortname = values[3]
        try:
            phone = int(values[4])
        except:
            phone = values[4]
        address = values[5]
        try:
            district = District.objects.get(name=district)
        except:
            district = District.objects.create(name=district)
        try:
            school = School.objects.create(INN=INN, name=name, shortname=shortname, phone=phone, address=address,
                                           district=district)
            SchoolUser.objects.create(username=INN, password=INN, school=school)
        except BaseException as ex:
            logger.debug(ex)


def update_schools_from_excel():
    dir = settings.BASE_DIR.__str__() + "\Spisok_OU_06_10_20.xlsx"
    rb = xlrd.open_workbook(dir)
    sheet = rb.sheet_by_index(0)
    for i in range(4, sheet.nrows):
        logger.info(str.format("import done {0}", int(float(i) / float(sheet.nrows) * 100)))
        values = sheet.row_values(i)
        INN = int(values[0])
        district = values[1]
        name = values[2]
        shortname = values[3]
        try:
            phone = int(values[4])
        except:
            phone = values[4]
        adress = values[5]
        try:
            district = District.objects.get(name=district)
        except:
            district = District.objects.create(name=district)
        try:
            school = School.objects.get(INN=INN)
            school.district = district
            school.name = name
            school.shortname = shortname
            school.phone = phone
            school.adress = adress
            school.save()
        except BaseException as err:
            print(err)


def make_export_file(data: dict):
    full_path = settings.DOCUMENT_ROOT + "/export.xls"
    excel = xlwt.Workbook()
    shit: Worksheet = excel.add_sheet("export", cell_overwrite_ok=True)
    schools = School.objects.all()
    districts = District.objects.all()
    row = START_ROW

    column = START_COLUMN
    cur_column = column

    if data.__contains__(School._meta.model_name):
        cur_data = data[School._meta.model_name]
        cur_data = json.loads(cur_data)
        fields = list(get_model_fields(School))
        for field in fields:
            if cur_data.__contains__(field.name):
                print(cur_data)
                if not cur_data[field.name]:
                    fields.remove(field)
            else:
                fields.remove(field)

        for school in schools:
            cur_column = column
            for field in fields:
                shit.write(2, cur_column, field.verbose_name.__str__())
                shit.write(row, cur_column, getattr(school, field.name).__str__())
                cur_column += 1
            row += 1

    excel.save(full_path)
    return full_path


def make_full_export_file():
    full_path = settings.DOCUMENT_ROOT + "/export.xls"
    excel = xlwt.Workbook()
    shit: Worksheet = excel.add_sheet("export", cell_overwrite_ok=True)
    schools = School.objects.all()
    districts = District.objects.all()
    row = START_ROW
    fields = get_model_fields(School)
    fields = fields[1:]
    column = 1
    cur_column = column
    for school in schools:
        cur_column = column
        for field in fields:
            shit.write(2, cur_column, field.verbose_name.__str__())
            shit.write(row, cur_column, getattr(school, field.name).__str__())
            cur_column += 1
        row += 1

    column = cur_column + 2
    row = START_ROW
    max_count = 0

    fields = list(get_model_fields(Building))
    for field in fields:
        if isinstance(field, models.ForeignKey):
            fields.remove(field)
    for school in schools:
        if max_count < len(school.building_set.all()):
            max_count = len(school.building_set.all())
    for school in schools:
        cur_column = column
        for building in school.building_set.all():
            shit.write(1, cur_column, building._meta.verbose_name)
            for field in fields:
                shit.write(2, cur_column, field.verbose_name.__str__())
                if getattr(building, field.name) is not None:
                    shit.write(row, cur_column, getattr(building, field.name).__str__())
                else:
                    shit.write(row, cur_column, "-")
                cur_column += 1
        row += 1

    excel.save(full_path)
    return full_path
