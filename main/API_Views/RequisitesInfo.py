from loguru import logger
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import RequisitesSerializer
from main.services import find_school_and_allow_user, get_requisites


class RequisitesInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
            requisites = get_requisites(school)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        requisites_serializer = RequisitesSerializer(requisites, many=False)
        return Response({'requisites': requisites_serializer.data})

    def put(self, request):
        data: dict = request.data
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
            requisites = get_requisites(school)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            requisites.update(data)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': ex.__str__()})
        logger.success(str.format("{0} Обновил информацию о {1}", user, school))
        return Response(status=status.HTTP_200_OK)
