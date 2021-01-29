from django.utils.dateparse import parse_date
from loguru import logger
from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from main.models import Temperature
from main.serializers.serializers import TemperatureSerializer
from main.services import find_school_and_allow_user, find_building_and_allow_user


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