from loguru import logger
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.indoor_areas import IndoorAreas
from main.serializers.indoor_areas_serializer import IndoorAreasSerializer
from main.services import find_building_and_allow_user


class IndoorAreasAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(building_id, user)
            ind_areas = IndoorAreas.objects.get_or_create(building=building)
            if ind_areas[1]:
                building.indoor_areas = ind_areas[0]
                building.save()
            ind_areas = ind_areas[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        ans = [IndoorAreasSerializer(ind_areas, many=False).data]
        print(ans)
        return Response(status=status.HTTP_200_OK, data=ans)

    def put(self, request):
        data = request.data
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(id=building_id, user=user)
            ind_areas = IndoorAreas.objects.get_or_create(building=building)
            if ind_areas[1]:
                building.indoor_areas = ind_areas[0]
                building.save()
            ind_areas = ind_areas[0]
            ind_areas.update(data=data)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        return Response(status=status.HTTP_200_OK)
