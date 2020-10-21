import xlrd, xlwt
from loguru import logger

from Egida import settings
from accounts.models import SchoolUser
from main.models import *
from django.db.utils import IntegrityError


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


def make_export_file(data):
    full_path = settings.DOCUMENT_ROOT + "/export.xls"
    excel = xlwt.Workbook()
    shit = excel.add_sheet("export")
    schools = School.objects.all()
    row = 4
    fields = get_model_fields(School)
    fields = fields[1:]

    column = 1
    # for field in fields:
    #     if data is None or data[field.name]:
    #         shit.write(2, column, field.verbose_name.__str__())
    #         column += 1
    #     else:
    #         fields.pop(field)
    for school in schools:
        column = 1
        for field in fields:
            shit.write(row, column, getattr(school, field.name).__str__())
            column += 1
        row += 1
    excel.save(full_path)
    return full_path
