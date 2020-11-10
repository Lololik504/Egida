import json

import xlrd
import xlwt
from loguru import logger
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
        address = values[5]
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
            school.address = address
            school.save()
        except BaseException as ex:
            logger.exception(ex)


class ExcelWriter(xlwt.Workbook):
    START_ROW = 4
    START_COLUMN = 1

    def __init__(self):
        super().__init__()
        self.row = START_ROW
        self.column = START_COLUMN
        self.shit: Worksheet = self.add_sheet("export", cell_overwrite_ok=True)
        self.schools = list(School.objects.all())
        self.full_path = settings.DOCUMENT_ROOT + "/export.xls"

    def add_model_to_excel(self, model: models.Model, data=None, many=True, full=False):
        if full:
            fields = list(get_model_fields(model))
        else:
            fields = self.filter_fields(data, model)
        next_column = self.column
        self.row = self.START_ROW
        get_atr_str = str(model._meta.model_name).lower()
        if many:
            get_atr_str += "_set"
        for school in self.schools:
            objects_list = list(school.__getattribute__(get_atr_str).all())
            for model_object in objects_list:
                cur_column = self.column
                for field in fields:
                    self.shit.write(2, cur_column, field.verbose_name.__str__())
                    self.shit.write(self.row, cur_column, getattr(model_object, field.name).__str__())
                    cur_column += 1
                self.row += 1
                if next_column < cur_column:
                    next_column = cur_column

        self.column = next_column

    def add_schools_to_excel(self, data=None, full=False):
        if full:
            fields = list(get_model_fields(School))
        else:
            fields = self.filter_fields(data, School)
        next_column = self.column
        self.row = self.START_ROW

        for model_object in self.schools:
            cur_column = self.column
            for field in fields:
                self.shit.write(2, cur_column, field.verbose_name.__str__())
                self.shit.write(self.row, cur_column, getattr(model_object, field.name).__str__())
                cur_column += 1
            self.row += 1
            if next_column < cur_column:
                next_column = cur_column

        self.column = next_column

    def filter_fields(self, data, model):
        if isinstance(data, str):
            data = json.loads(data)
        fields = list(get_model_fields(model))
        fields = list(filter(lambda f_field: data.__contains__(f_field.name), fields))
        fields = list(filter(lambda f_field: data[f_field.name], fields))
        return fields

    def filter_schools(self):
        pass

    def make_export_file(self, data: dict):
        self.filter_schools()
        if data.__contains__(School._meta.model_name):
            self.add_schools_to_excel(data=data[School._meta.model_name])
        if data.__contains__(Building._meta.model_name):
            self.add_model_to_excel(data=data[Building._meta.model_name], model=Building(), many=True)
        self.save(self.full_path)
        return self.full_path

    def make_full_export_file(self):
        self.add_schools_to_excel(full=True)
        self.add_model_to_excel(model=Building(), many=True, full=True)
        self.save(self.full_path)
        return self.full_path


def make_export_file(data: dict):
    excel = ExcelWriter()
    return excel.make_export_file(data)

    # full_path = settings.DOCUMENT_ROOT + "/export.xls"
    # excel = xlwt.Workbook()
    # shit: Worksheet = excel.add_sheet("export", cell_overwrite_ok=True)
    # schools = School.objects.all()
    # districts = District.objects.all()
    # row = START_ROW
    #
    # column = START_COLUMN
    # next_column = column
    #
    # if data.__contains__(School._meta.model_name):
    #     cur_data = data[School._meta.model_name]
    #     if isinstance(cur_data, str):
    #         cur_data = json.loads(cur_data)
    #     fields = list(get_model_fields(School))
    #     fields = filter(lambda filter_field: cur_data.__contains__(filter_field.name), fields)
    #     fields = list(filter(lambda filter_field: cur_data[filter_field.name], fields))
    #
    #     for school in schools:
    #         cur_column = column
    #
    #         for field in fields:
    #             shit.write(2, cur_column, field.verbose_name.__str__())
    #             shit.write(row, cur_column, getattr(school, field.name).__str__())
    #             cur_column += 1
    #         row += 1
    #         if next_column < cur_column:
    #             next_column = cur_column
    #
    # column = next_column
    # row = START_ROW
    #
    # if data.__contains__(Building._meta.model_name):
    #     cur_data = data[Building._meta.model_name]
    #     if isinstance(cur_data, str):
    #         cur_data = json.loads(cur_data)
    #     fields = list(get_model_fields(Building))
    #     fields = filter(lambda field: cur_data.__contains__(field.name), fields)
    #     fields = list(filter(lambda field: cur_data[field.name], fields))
    #
    #     for school in schools:
    #         cur_column = column
    #         for building in school.building_set.all():
    #             shit.write(1, cur_column, "Здание")
    #             for field in fields:
    #                 shit.write(2, cur_column, field.verbose_name.__str__())
    #                 shit.write(row, cur_column, getattr(building, field.name).__str__())
    #                 cur_column += 1
    #         if cur_column > next_column:
    #             next_column = cur_column
    #         row += 1
    #
    # excel.save(full_path)
    # return full_path


def make_full_export_file():
    excel = ExcelWriter()
    return excel.make_full_export_file()

    # full_path = settings.DOCUMENT_ROOT + "/export.xls"
    # excel = xlwt.Workbook()
    # shit: Worksheet = excel.add_sheet("export", cell_overwrite_ok=True)
    # schools = School.objects.all()
    # districts = District.objects.all()
    # row = START_ROW
    # fields = get_model_fields(School)
    # fields = fields[1:]
    # column = 1
    # cur_column = column
    # for school in schools:
    #     cur_column = column
    #     for field in fields:
    #         shit.write(2, cur_column, field.verbose_name.__str__())
    #         shit.write(row, cur_column, getattr(school, field.name).__str__())
    #         cur_column += 1
    #     row += 1
    #
    # column = cur_column + 2
    # row = START_ROW
    # max_count = 0
    #
    # fields = list(get_model_fields(Building))
    # for field in fields:
    #     if isinstance(field, models.ForeignKey):
    #         fields.remove(field)
    # for school in schools:
    #     if max_count < len(school.building_set.all()):
    #         max_count = len(school.building_set.all())
    # for school in schools:
    #     cur_column = column
    #     for building in school.building_set.all():
    #         shit.write(1, cur_column, building._meta.verbose_name)
    #         for field in fields:
    #             shit.write(2, cur_column, field.verbose_name.__str__())
    #             if getattr(building, field.name) is not None:
    #                 shit.write(row, cur_column, getattr(building, field.name).__str__())
    #             else:
    #                 shit.write(row, cur_column, "-")
    #             cur_column += 1
    #     row += 1
    #
    # excel.save(full_path)
    # return full_path
