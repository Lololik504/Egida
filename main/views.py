from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from accounts.services import *
from .translit import latinizator
from accounts import excel


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
        print(request)
        data = request.headers
        print(data)
        print(request.headers)
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


def test(request):
    excel.create_new_schools_and_users_from_excel()
    return redirect(reverse('start_page'))

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


def districts_api(request):
    districts = DistrictsSerializer(District.objects.all(), many=True).data
    return JsonResponse({'districts': districts})


def schools_in_district_api(request, district_name):
    schools = list(filter(lambda school: school.district.name == district_name, School.objects.all()))
    schools = SchoolsSerializer(schools, many=True).data
    return JsonResponse({'schools': schools})
