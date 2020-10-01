from django.core import serializers
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import District, School
from .serializers import DistrictsSerializer, SchoolsSerializer
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


def districts_api(request):
    districts = DistrictsSerializer(District.objects.all(), many=True).data
    return JsonResponse({'districts': districts})


def schools_in_district_api(request, district_name):
    schools = list(filter(lambda school: school.district.name == district_name, School.objects.all()))
    schools = SchoolsSerializer(schools, many=True).data
    return JsonResponse({'schools': schools})
