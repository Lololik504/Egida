from loguru import logger
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.accessible_environment import AccessibleEnvironment
from main.serializers.accessible_environment_serializer import AccessibleEnvironmentSerializer
from main.services import find_building_and_allow_user


class AccessibleEnvironmentAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(building_id, user)
            access_environ = AccessibleEnvironment.objects.get_or_create(building=building)
            if access_environ[1]:
                building.accessible_environment = access_environ[0]
                building.save()
            access_environ = access_environ[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        ans = [AccessibleEnvironmentSerializer(access_environ, many=False).data]
        return Response(status=status.HTTP_200_OK, data=ans)

    def put(self, request):
        data = request.data
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(id=building_id, user=user)
            access_environ = AccessibleEnvironment.objects.get_or_create(building=building)
            if access_environ[1]:
                building.accessible_environment = access_environ[0]
                building.save()
            access_environ = access_environ[0]
            access_environ.update(data=data)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        return Response(status=status.HTTP_200_OK)
