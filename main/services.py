from django.urls import resolve
from .models import School, District


def get_current_district(request):
    current_url = request.path_info
    last_in_url = (get_last_in_url(current_url))
    return last_in_url


def get_last_in_url(url):
    counter = 0
    for i in reversed(url):
        if i == '/':
            break
        counter += 1
    last = url[-counter:]
    return last


def get_schools_by_district(district):
    schools = School.objects.all()
    schools = filter((lambda f: f.district == district), schools)
    return schools
