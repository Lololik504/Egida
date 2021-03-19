from loguru import logger
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.engineering_communication import EngineeringCommunication
from main.serializers.engineering_communication_serializer import EngineeringCommunicationSerializer
from main.services import find_building_and_allow_user


class EngineeringCommunicationAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(building_id, user)
            eng_communication = EngineeringCommunication.objects.get_or_create(building=building)
            if eng_communication[1]:
                building.engineering_communication = eng_communication[0]
                building.save()
            eng_communication = eng_communication[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        ans = [EngineeringCommunicationSerializer(eng_communication, many=False).data]
        return Response(status=status.HTTP_200_OK, data=ans)

    def put(self, request):
        data = request.data
        building_id = data['id']
        user = request.my_user
        if request.FILES:
            files = request.FILES
            data.update(files)
        try:
            building = find_building_and_allow_user(id=building_id, user=user)
            eng_communication = EngineeringCommunication.objects.get_or_create(building=building)
            if eng_communication[1]:
                building.engineering_communication = eng_communication[0]
                building.save()
            eng_communication = eng_communication[0]
            eng_communication.update(data=data)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        return Response(status=status.HTTP_200_OK)
