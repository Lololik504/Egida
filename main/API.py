from loguru import logger
from rest_framework import permissions
from rest_framework.views import APIView
from main.allows import *
from main.serializers import *
from main.services import export, find_school_and_allow_user


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
        logger.success(str.format("{0} Добавил информацию о зданиях {1}\n{2}", user, school, building))
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
        except BaseException as ex:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            buildings = list(filter(lambda b: b.school == school, Building.objects.all()))
        except:
            return Response(data=[])
        ans = []
        buildings_serializer = BuildingAllInfoSerializer(buildings, many=True)
        ans.append(buildings_serializer.data)
        logger.success(str.format("{0} Получил информацию о зданиях {1}", user, school))
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
        logger.success(str.format("{0} Изменил информацию о здании {1}\n{2}", user, building.school, building))
        return Response(status=status.HTTP_200_OK)


class SchoolInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
        except BaseException as ex:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        school_serializer = SchoolAllInfoSerializer(school, many=False)
        logger.success(str.format("{0} Получил информацию о {1}", user, school))
        return Response({'school': school_serializer.data})

    def put(self, request):
        data: dict = request.data
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
        except BaseException as ex:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            school.update(data)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Error with update method'})
        logger.success(str.format("{0} Обновил информацию о {1}", user, school))
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
        logger.success(str.format("{0} Добавил информацию о {1}", user, school))
        return Response(status=status.HTTP_200_OK)


class DistrictsInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = request.my_user
        if not departament_allow(user):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        else:
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
            logger.success(str.format("{0} Получил информацию о всех районах", user))
            return Response(ans)


class OneDistrictInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = request.my_user
        district_name = request.headers['district']
        try:
            district = District.objects.get(name=district_name)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Cant find district'})
        if district_allow(user, district):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        else:
            try:
                schools = district.school_set.all()
                district_serializer = DistrictsSerializer(district, many=False)
                schools_serializer = SchoolInfoSerializer(schools, many=True)
                ans = {
                    'district': district_serializer.data,
                    'schools': schools_serializer.data
                }
                logger.success(str.format("{0} Получил информацию о {1}", user, district))
                return Response(ans)
            except BaseException as ex:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})


class DirectorInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        user = request.my_user
        INN = request['INN']
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
            director = Director.objects.create(**data, school=school)
        except BaseException as ex:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': ex.__str__()})
        logger.success(str.format("{0} Добавил информацию о директоре {1}", user, school))
        return Response(status=status.HTTP_200_OK)


class ExportExcel(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.data
        user = request.my_user
        if (user == None):
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        if not (departament_allow(user)):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        resp = export(data)
        return resp
