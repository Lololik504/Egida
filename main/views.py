from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import District, School
from accounts.models import SchoolUser
from accounts.serializers import UserSerialiaer
from accounts.license import IsSchoolProfile, IsDistrictProfile
from .serializers import *
from .services import *
from .translit import latinizator


# Create your views here.

class Districts(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        districts = District.objects.all()
        serializer = DistrictsSerializer(districts, many=True)
        return Response(serializer.data)


class Schools(APIView):
    def get(self, request, district_name):
        schools = School.objects.all()
        serializer = SchoolsSerializer(schools, many=True)
        return Response(serializer.data)


class School(APIView):
    permission_classes = [IsSchoolProfile, permissions.IsAuthenticated]

    def get(self, request, INN):
        asker = request.headers.get('username')
        user = list(filter(lambda school: school.username == asker, SchoolUser.objects.all()))
        if len(user) == 1:
            user = user[0]
            user_serializer = UserSerialiaer(user, many=False)
            return Response({'user': user_serializer.data})
        else:
            response = Response(status=405)
            return response


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
