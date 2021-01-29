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
        id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(id, user)
            building_constr = BuildingConstruction.objects.get_or_create(building=building)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})

        ans = []
        ans += BuildingConstructionSerializer(building_constr).data
        return Response(ans)
