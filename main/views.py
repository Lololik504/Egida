from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from accounts.serializers import UserSerialiaer
from accounts.license import Permissions
from accounts.models import SchoolUser
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
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, INN):
        data = request.headers
        username = data['username']
        INN = data['INN']
        token = data['Authorization']
        token = token.split()[1]
        try:
            user = User.objects.get(username=username)
            if user.auth_token.key == token:
                user = get_user_class(username)
                if user.permission == Permissions.school.value:
                    school = user.school
                else:
                    try:
                        school = School.objects.get(INN=INN)
                    except:
                        return Response(status=status.HTTP_401_UNAUTHORIZED)
                school_serialiser = SchoolsSerializer(school, many=False)
                return Response({'school': school_serialiser.data})
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


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
