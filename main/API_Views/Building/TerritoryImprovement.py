from loguru import logger
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.territory_improvement import TerritoryImprovement
from main.serializers.territory_improvement_serializator import TerritoryImprovementSerializer
from main.services import find_building_and_allow_user


class TerritoryImprovementAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(building_id, user)
            ter_imp = TerritoryImprovement.objects.get_or_create(building=building)
            if ter_imp[1]:
                building.territory_improvement = ter_imp[0]
                building.save()
            ter_imp = ter_imp[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        ans = [TerritoryImprovementSerializer(ter_imp, many=False).data]
        return Response(status=status.HTTP_200_OK, data=ans)

    def put(self, request):
        data = request.data
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(id=building_id, user=user)
            ter_imp = TerritoryImprovement.objects.get_or_create(building=building)
            if ter_imp[1]:
                building.territory_improvement = ter_imp[0]
                building.save()
            ter_imp = ter_imp[0]
            ter_imp.update(data=data)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        return Response(status=status.HTTP_200_OK)
