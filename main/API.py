from django.http.request import HttpHeaders
from loguru import logger
from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from django.utils.dateparse import parse_date

from main.allows import *
from main.serializers import *
from main.services import *


class BuildingInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request):
        data: dict = request.data
        try:
            data.pop('school')
        except:
            pass
        INN = data.pop('INN')
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        try:
            school = School.objects.get(INN=INN)
        except BaseException as ex:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': ex.__str__()})
        if not departament_allow(user):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        try:
            building = Building.objects.create(school=school)
            building.update(data=data)
            building.save()
            logger.success(str.format("{0} Добавил информацию о зданиях {1}\n{2}", user, school, building))
            return Response(status=status.HTTP_200_OK)
        except BaseException as ex:
            try:
                building.delete()
            except:
                pass
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED,
                            data={'detail': ex.__str__()})

    def get(self, request):
        data = request.headers
        id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(id, user)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        ans = []
        building_serializer = BuildingAllInfoSerializer(building, many=False)
        ans.append(building_serializer.data)
        logger.success(str.format("{0} Получил информацию о здании {1}", user, building))
        return Response(data=ans)

    def put(self, request):
        data: dict = request.data
        id = data['id']
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        try:
            building = Building.objects.get(id=id)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Cant find school with this INN'})
        if not building_allow(building, user):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        try:
            building.update(data)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Error with update method'})
        logger.success(str.format("{0} Изменил информацию о здании {1}\n{2}", user, building.school, building))
        return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        data = request.headers
        id = data['id']
        user = request.my_user
        if not departament_allow(user):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        try:
            building = find_building_and_allow_user(id, user)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            building.delete()
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        return Response(status=status.HTTP_200_OK)


class TemperatureInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        buildings = school.building_set.all()
        ans: dict = {}
        for building in buildings:
            temp_info = building.temperature_set.all()
            ans.update({building.id: TemperatureSerializer(temp_info, many=True).data})
        logger.success(str.format("{0} Получил информацию о температурном режиме {1}", user, school))
        return Response(data=ans)

    def post(self, request: Request):
        global new_temper
        data: dict = request.data
        try:
            data.pop('id')
        except:
            pass
        building_id = data.pop('building')
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        try:
            building_obj = find_building_and_allow_user(building_id, user)
        except BaseException as ex:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': ex.__str__()})
        try:
            new_temper = Temperature.objects.create(building=building_obj, **data)
            new_temper.save()
            logger.success(
                str.format("{0} Добавил информацию о температуре здания {1}\n{2}", user, building_obj, new_temper))
            return Response(status=status.HTTP_200_OK)
        except BaseException as ex1:
            try:
                new_temper.delete()
                logger.exception(ex1)
                return Response(status=status.HTTP_501_NOT_IMPLEMENTED,
                                data={'detail': ex1.__str__()})
            except BaseException as ex2:
                logger.exception(ex2)
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED,
                            data={'detail': ex2.__str__()})

    def delete(self, request):
        data: dict = request.headers['data']
        if isinstance(data, str):
            data = json.loads(data)
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        temp_date = data['date']
        building_id = data['building']
        temp_objs = Temperature.objects.all()
        temp_objs = list(filter(lambda t: t.date == parse_date(temp_date), temp_objs))

        temp_objs = list(filter(lambda t: t.building.id == int(building_id), temp_objs))

        building_obj = find_building_and_allow_user(building_id, user)
        try:
            if isinstance(temp_objs, list):
                for temp_obj in temp_objs:
                    temp_obj.delete()
            else:
                temp_objs.delete()
                logger.success(
                    str.format("{0} Добавил информацию о температуре здания {1} по дате {2}\n", user, building_obj,
                               temp_date))
            return Response(status=status.HTTP_200_OK)
        except BaseException as ex:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': ex.__str__()})

    def put(self, request: Request):
        data: dict = request.data
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        temp_id = data.pop('id')
        data.pop('building')
        temp_obj = Temperature.objects.get(id=temp_id)
        try:
            find_building_and_allow_user(temp_obj.building_id, user)
            temp_obj.update(data)
            return Response(status=status.HTTP_200_OK)
        except BaseException as ex:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': ex.__str__()})


class SchoolBuildingsInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            buildings = list(filter(lambda b: b.school == school, Building.objects.all()))
        except BaseException as ex:
            logger.exception(ex)
            return Response(data=[])
        ans = []
        buildings_serializer = BuildingSerializer(buildings, many=True)
        ans.append(buildings_serializer.data)
        logger.success(str.format("{0} Получил информацию о зданиях {1}", user, school))
        return Response(data=ans)


class SchoolInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
        except BaseException as ex:
            logger.exception(ex)
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
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            school.update(data)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': ex.__str__()})
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
            school = School.create(**data)
            SchoolUser.objects.create(username=school.INN, password=school.INN, school=school)

        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': ex.__str__()})
        logger.success(str.format("{0} Добавил информацию о {1}", user, school))
        return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        data: dict = request.headers
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        if user.permission > MyUser.Permissions.DISTRICT.value:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        try:
            school = School.objects.get(INN=data['INN'])
            if not (district_allow(user, school.district)):
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                                data={'detail': 'You dont have permission to do this'})
            school.delete()
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': ex.__str__()})
        logger.success(str.format("{0} Удалил информацию о {1}", user, school))
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
            ans = []
            for district in districts:
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
        except BaseException as ex:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': ex.__str__()})
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


class PersonalOfSchoolInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        director = get_director(school)
        bookkeeper = get_bookkeeper(school)
        responsible_for_filling = get_updater(school)
        zavhoz = get_zavhoz(school)
        ans = {}
        ans.update({get_model_name(director): PersonalAllInfoSerializer(director, many=False).data})
        ans.update({get_model_name(zavhoz): PersonalAllInfoSerializer(zavhoz, many=False).data})
        ans.update({get_model_name(bookkeeper): PersonalAllInfoSerializer(bookkeeper, many=False).data})
        ans.update({get_model_name(responsible_for_filling): PersonalAllInfoSerializer(responsible_for_filling,
                                                                                       many=False).data})
        return Response(data=ans)

    def put(self, request):
        data = request.data
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        director = get_director(school)
        bookkeeper = get_bookkeeper(school)
        responsible_for_filling = get_updater(school)
        zavhoz = get_zavhoz(school)
        try:
            director.update(data[get_model_name(director)])
            zavhoz.update(data.pop(get_model_name(zavhoz)))
            bookkeeper.update(data.pop(get_model_name(bookkeeper)))
            responsible_for_filling.update(data.pop(get_model_name(responsible_for_filling)))
        except BaseException as ex:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})

        return Response(status=status.HTTP_200_OK)


class ExportExcel(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data: dict = request.headers['data']
        if isinstance(data, str):
            data = json.loads(data)
        user = request.my_user
        if (user == None):
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        if not (departament_allow(user)):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        if not data.__contains__("full"):
            resp = export(data)
        else:
            resp = full_export()
        # resp = full_export()
        return resp


class TEST(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        date = parse_date("2010-10-31")
        return Response(status=status.HTTP_200_OK)
