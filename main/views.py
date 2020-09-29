from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from .models import District, School
from .serializers import MainSerializer
from .services import *
from .translit import latinizator


# Create your views here.

def index(request):
    districts = District.objects.all()
    urls = []
    for district in districts:
        print(districts)
        urls.append(latinizator(district.name))
    context = {
        'districts': districts,
        'urls': urls
    }
    return render(request, 'main/index.html', context)


def district(request, url):
    require_dist = District.objects.filter(name=url)[0]
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


class HomeView(ModelViewSet):
    queryset = District.objects.all()
    serializer_class = MainSerializer


def district_app(request):
    return render(request, 'main/empty.html')