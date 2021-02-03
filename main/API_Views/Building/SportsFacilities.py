from loguru import logger
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.sports_facilities import SportsFacilities
from main.serializers.sports_facilities_serializer import SportsFacilitiesSerializer
from main.services import find_building_and_allow_user


class SportsFacilitiesAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(building_id, user)
            sport_fac = SportsFacilities.objects.get_or_create(building=building)
            if sport_fac[1]:
                building.sports_facilities = sport_fac[0]
                building.save()
            sport_fac = sport_fac[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        ans = [SportsFacilitiesSerializer(sport_fac, many=False).data]
        return Response(status=status.HTTP_200_OK, data=ans)

    def put(self, request):
        data = request.data
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(id=building_id, user=user)
            sport_fac = SportsFacilities.objects.get_or_create(building=building)
            if sport_fac[1]:
                building.sports_facilities = sport_fac[0]
                building.save()
            sport_fac = sport_fac[0]
            sport_fac.update(data=data)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        return Response(status=status.HTTP_200_OK)
