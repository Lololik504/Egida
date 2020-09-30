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


class DistrictsApi(ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictsSerializer


class SchoolsApi(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolsSerializer



def district_app(request):
    districts = DistrictsSerializer(District.objects.all(), many=True).data
    print(districts)
    return JsonResponse({'districts': districts})
