from django.shortcuts import render, HttpResponse
from .models import District, School
from .services import *
from .translit import latinizator


# Create your views here.

def index(request):
    districts = District.objects.all()
    urls = []
    for district in districts:
        urls.append(latinizator(district.name))
    context = {
        'districts': districts,
        'urls': urls
    }
    return render(request, 'main/index.html', context)


def district(request, url):
    districts = District.objects.all()
    require_list = list(filter((lambda f: f.name == url), districts))
    if len(require_list) == 1:
        require_dist = require_list[0]
    else:
        return render(request, 'main/index.html')
    schools = get_schools_by_district(require_dist)
    context = {
        'district': require_dist,
        'schools': schools
    }
    return render(request, 'main/district.html', context)


def school(request, url, id):
    school = get_school_by_id(id)
    context = {
        'school': school
    }
    return render(request, 'main/school.html', context)
