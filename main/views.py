from urllib.request import Request

from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.backends import MyAuthentication
from accounts.services import *
from .allows import *
from .services import update_school
from accounts import excel
from .serializers import *


class SchoolInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, INN):
        data = request.headers
        INN = data['INN']
        user_token = MyAuthentication.authenticate(MyAuthentication(), request)
        user = user_token[0]
        user = get_user_class(user)
        try:
            school = School.objects.get(INN=INN)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Cant find school with this INN'})
        if not school_allow(user, school):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        school_serializer = SchoolAllInfoSerializer(school, many=False)
        return Response({'school': school_serializer.data})

    def post(self, request):
        data = request.headers
        INN = data['INN']
        user_token = MyAuthentication.authenticate(MyAuthentication(), request)
        user = user_token[0]
        user = get_user_class(user)
        try:
            school = School.objects.get(INN=INN)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Cant find school with this INN'})
        if not school_allow(user, school):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        update_school(school, data)
        return Response(status=status.HTTP_200_OK)


class DistrictsInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user_token = MyAuthentication.authenticate(MyAuthentication(), request)
        user = user_token[0]
        user = get_user_class(user)
        if user.permission <= Permissions.departament.value:
            districts = District.objects.all()
            schools = School.objects.all()
            district_serializer = DistrictsSerializer(districts, many=True)
            school_serializer = SchoolInfoSerializer(schools, many=True)
            ans = {
                'districts': district_serializer.data,
                'schools': school_serializer.data
            }
            return Response(ans)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})


class OneDistrictInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: Request):
        user_token = MyAuthentication.authenticate(MyAuthentication(), request)
        user = user_token[0]
        user = get_user_class(user)
        district_name = request.headers['district']
        if user.permission <= Permissions.district.value:
            try:
                if isinstance(user, DistrictUser):
                    district = user.district
                    if district_name != district.name:
                        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                                        data={'detail': 'You dont have permission to do this'})
                else:
                    district = District.objects.get(name=district_name)
                schools = School.objects.get(district=district)
                district_serializer = DistrictsSerializer(district, many=False)
                schools_serializer = SchoolInfoSerializer(schools, many=True)
                ans = {
                    'district': district_serializer.data,
                    'schools': schools_serializer.data
                }
                return Response(ans)
            except:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def test(request):
    excel.create_new_schools_and_users_from_excel()
    return redirect(reverse('start_page'))


def index(request):
    districts = District.objects.all()
    urls = []
    for district in districts:
        urls.append(district.name)
    context = {
        'districts': districts,
        'urls': urls
    }
    return render(request, 'main/index.html', context)
