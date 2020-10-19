import os

from django.http import HttpResponse
from loguru import logger

from Egida import settings
from main import excel
from main.allows import school_allow
from main.models import School


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


def export(data=None):
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
