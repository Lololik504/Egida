from loguru import logger
from requests import Response
from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.views import APIView

from main.allows import building_allow
from main.models import Building
from main.serializers import BuildingAllInfoSerializer, BuildingSerializer
from main.services import find_school_and_allow_user, find_building_and_allow_user


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
            school = find_school_and_allow_user(INN=INN, user=user)
        except BaseException as ex:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': ex.__str__()})
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
        id = data.pop('id')
        print(data)
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