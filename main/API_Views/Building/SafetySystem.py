from loguru import logger
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.safety_system import SafetySystem
from main.serializers.safety_system_serializer import SafetySystemSerializer
from main.services import find_building_and_allow_user


class SafetySystemAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(building_id, user)
            safety_sys = SafetySystem.objects.get_or_create(building=building)
            if safety_sys[1]:
                building.safety_system = safety_sys[0]
                building.save()
            safety_sys = safety_sys[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        ans = [SafetySystemSerializer(safety_sys, many=False).data]
        print(ans)
        return Response(status=status.HTTP_200_OK, data=ans)

    def put(self, request):
        data = request.data
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(id=building_id, user=user)
            safety_sys = SafetySystem.objects.get_or_create(building=building)
            if safety_sys[1]:
                building.safety_systems = safety_sys[0]
                building.save()
            safety_sys = safety_sys[0]
            safety_sys.update(data=data)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        return Response(status=status.HTTP_200_OK)
