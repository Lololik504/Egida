from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.services import MyUser, DistrictUser, SchoolUser
from main.allows import school_allow, departament_allow, building_allow
from main.serializers import *


class BuildingInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request
        INN = data['INN']
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        try:
            school = School.objects.get(INN=INN)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Cant find school with this INN'})
        if not school_allow(user, school):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        building = Building.objects.create(school=school)
        building.update(data=data)
        building.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        try:
            school = School.objects.get(INN=INN)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Cant find school with this INN'})
        if not school_allow(user, school):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        try:
            buildings = list(filter(lambda b: b.school == school, Building.objects.all()))
        except:
            print(Building.PURPOSE.values)
            return Response(data=[])
        ans = []
        ans.append(Building.get_choices(Building()))
        buildings_serializer = BuildongAllInfoSerializer(buildings, many=True)
        ans.append(buildings_serializer.data)
        return Response(ans)

    def put(self, request):
        data: dict = request.data
        id = data['id']
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        try:
            building = Building.objects.get(id=id)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Cant find school with this INN'})
        if not building_allow(user, building):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        try:
            building.update(data)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Error with update method'})
        return Response(status=status.HTTP_200_OK)


class SchoolInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
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

    def put(self, request):
        data: dict = request.data
        INN = data['INN']
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        try:
            school = School.objects.get(INN=INN)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Cant find school with this INN'})
        if not school_allow(user, school):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        try:
            school.update(data)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Error with update method'})
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        data: dict = request.data
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        if user.permission > MyUser.Permissions.DISTRICT.value:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        try:
            school = School.objects.create(**data)
            SchoolUser.objects.create(username=school.INN, password=school.INN, school=school)
        except BaseException as err:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': err.__str__()})
        return Response(status=status.HTTP_200_OK)


class DistrictsInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = request.my_user
        if departament_allow(user):
            districts = District.objects.all()
            schools = School.objects.all()
            ans = []
            for district in districts:
                # dist_schools = list(filter(lambda school: school.district == district, schools))
                dist_schools = district.school_set.all()
                ans.append({
                    'name': DistrictsSerializer(district, many=False).data,
                    'schools': SchoolInfoSerializer(dist_schools, many=True).data
                })

            return Response(ans)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})


class OneDistrictInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = request.my_user
        district_name = request.headers['district']
        if user.permission <= MyUser.Permissions.district.value:
            try:
                if isinstance(user, DistrictUser):
                    district = user.district
                    if district_name != district.name:
                        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                                        data={'detail': 'You dont have permission to do this'})
                else:
                    district = District.objects.get(name=district_name)
                schools = district.school_set.all()
                district_serializer = DistrictsSerializer(district, many=False)
                schools_serializer = SchoolInfoSerializer(schools, many=True)
                ans = {
                    'district': district_serializer.data,
                    'schools': schools_serializer.data
                }
                return Response(ans)
            except:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DirectorInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        user = request.my_user
        INN = request['INN']
        try:
            school = School.objects.get(INN=INN)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Cant find school with this INN'})
        if not school_allow(user, school):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        try:
            director = Director.objects.create(**data, school=school)
        except BaseException as err:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': err.__str__()})
        return Response(status=status.HTTP_200_OK)
