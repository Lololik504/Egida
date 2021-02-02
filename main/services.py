import os

from django.http import HttpResponse

from Egida import settings
from main import excel
from main.allows import school_allow, building_allow
from main.models import *
from main.models import Director, Bookkeeper
from main.models.PersonalModel import Updater, ZavHoz


def imp(f):
    # direct = settings.BASE_DIR.__str__() + 'main/docs/import.xls'
    direct = settings.BASE_DIR.__str__() + '/main/docs/'
    if not (os.path.exists(direct)):
        os.mkdir(direct)
    direct += 'import.xls'
    with open('main/docs/import.xls', 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    excel.create_new_schools_and_users_from_excel(direct)


def full_export():
    content = excel.make_full_export_file()
    response = HttpResponse(open(content, 'rb'), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = "filename=export.xls"
    return response


def export(data):
    content = excel.make_export_file(data)
    response = HttpResponse(open(content, 'rb'), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = "filename=export.xls"
    return response


def find_school_and_allow_user(INN, user):
    if user is None:
        raise BaseException('You need to authorize')
    try:
        school = School.objects.get(INN=INN)
    except:
        raise BaseException('Cant find school with this INN')
    if not school_allow(user, school):
        raise BaseException('You dont have permission to do this')
    return school


def find_building_and_allow_user(id, user):
    if user is None:
        raise BaseException('You need to authorize')
    try:
        building = Building.objects.get(id=id)
    except BaseException as ex:
        raise ex
    if not building_allow(building, user):
        raise BaseException('You dont have permission to do this')
    return building


def get_director(school: School):
    try:
        director = school.director
    except Director.DoesNotExist as ex:
        director = Director.objects.create(school=school)
    return director

def get_requisites(school: School):
    try:
        requisites = school.requisites
    except Requisites.DoesNotExist as ex:
        requisites = Requisites.objects.create(school=school)
    return requisites

def get_bookkeeper(school: School):
    try:
        bookkeeper = school.bookkeeper
    except Bookkeeper.DoesNotExist as ex:
        bookkeeper = Bookkeeper.objects.create(school=school)
    return bookkeeper


def get_updater(school: School):
    try:
        updater = school.updater
    except Updater.DoesNotExist as ex:
        updater = Updater.objects.create(school=school)
    return updater


def get_zavhoz(school: School):
    try:
        zavhoz = school.zavhoz
    except ZavHoz.DoesNotExist as ex:
        zavhoz = ZavHoz.objects.create(school=school)
    return zavhoz

