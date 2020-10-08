import xlrd, xlwt
from Egida import settings
from accounts.models import SchoolUser
from main.models import School, District
from django.db.utils import IntegrityError


def create_new_schools_and_users_from_excel():
    dir = settings.BASE_DIR.__str__() + "\\Spisok_OU_06_10_20.xlsx"
    rb = xlrd.open_workbook(dir)
    sheet = rb.sheet_by_index(0)
    for i in range(4, sheet.nrows):
        print(int(float(i) / float(sheet.nrows) * 100))
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
            school = School.objects.create(INN=INN, name=name, shortname=shortname, phone=phone, adress=adress,
                                           district=district)
            SchoolUser.objects.create(username=INN, password=INN, school=school)
        except BaseException as err:
            # print(err, 2)
            pass


def update_schools_from_excel():
    dir = settings.BASE_DIR.__str__() + "\\Spisok_OU_06_10_20.xlsx"
    rb = xlrd.open_workbook(dir)
    sheet = rb.sheet_by_index(0)
    for i in range(4, sheet.nrows):
        print(int(float(i) / float(sheet.nrows) * 100))
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