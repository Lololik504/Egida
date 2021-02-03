from loguru import logger
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.building_construction import BuildingConstruction
from main.services import find_building_and_allow_user
from main.serializers.building_construction_serializer import *


class BuildingConstructionAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(building_id, user)
            building_constr = BuildingConstruction.objects.get_or_create(building=building)
            if building_constr[1]:
                building.building_construction = building_constr[0]
                building.save()
            building_constr = building_constr[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        ans = [BuildingConstructionSerializer(building_constr, many=False).data]
        return Response(status=status.HTTP_200_OK, data=ans)

    def put(self, request):
        data = request.data
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(id=building_id, user=user)
            building_constr = BuildingConstruction.objects.get_or_create(building=building)
            if building_constr[1]:
                building.building_construction = building_constr[0]
                building.save()
            building_constr = building_constr[0]
            building_constr.update(data=data)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        return Response(status=status.HTTP_200_OK)
