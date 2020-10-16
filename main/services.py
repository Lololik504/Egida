import os

from django.http import HttpResponse

from Egida import settings
from main import excel


def imp(f):
    direct = settings.BASE_DIR.__str__() + 'main/docs/import.xlsx'
    if not (os.path.exists('main/docs')):
        os.mkdir('main/docs')
    with open('main/docs/import.xlsx', 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    excel.create_new_schools_and_users_from_excel(direct)


def export():
    content = excel.make_export_file()
    response = HttpResponse(open(content, 'rb'), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = "filename=export.xls"
    return response
    pass
