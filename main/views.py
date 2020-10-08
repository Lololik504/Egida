from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.backends import MyAuthentication
from accounts.services import *
from .translit import latinizator
from accounts import excel
from accounts import services


# Create your views here.

# class Districts(APIView):
#     # permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request):
#         districts = District.objects.all()
#         serializer = DistrictsSerializer(districts, many=True)
#         return Response(serializer.data)


# class Schools(APIView):
#     def get(self, request, district_name):
#         schools = School.objects.all()
#         serializer = SchoolsSerializer(schools, many=True)
#         return Response(serializer.data)


# class School(APIView): old API
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request, INN):
#         print(request)
#         data = request.headers
#         print(data)
#         print(request.headers)
#         username = data['username']
#         INN = data['INN']
#         token = data['Authorization']
#         token = token.split()[1]
#         try:
#             user = User.objects.get(username=username)
#             if user.auth_token.key == token:
#                 user = get_user_class(username)
#                 if user.permission == Permissions.school.value:
#                     school = user.school
#                 else:
#                     try:
#                         school = School.objects.get(INN=INN)
#                     except:
#                         return Response(status=status.HTTP_401_UNAUTHORIZED)
#                 school_serialiser = SchoolsSerializer(school, many=False)
#                 return Response({'school': school_serialiser.data})
#             else:
#                 return Response(status=status.HTTP_401_UNAUTHORIZED)
#         except:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)


class SchoolInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, INN):
        data = request.headers
        INN = data['INN']
        user_token = MyAuthentication.authenticate(MyAuthentication(), request)
        user = user_token[0]
        user = services.get_user_class(user)
        try:
            if type(user) == SchoolUser:
                school = user.school
            elif user.permission <= Permissions.school.value:
                try:
                    school = School.objects.get(INN=INN)
                except:
                    return Response(status=status.HTTP_401_UNAUTHORIZED,
                                    headers={'detail: school with this INN does not exist'})
            else:
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                                headers={'detail: you dont have permission to do this'})
            school_serializer = SchoolsSerializer(school, many=False)
            return Response({'school': school_serializer.data})
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

