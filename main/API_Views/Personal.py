from loguru import logger
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import get_model_name
from main.serializers import PersonalAllInfoSerializer
from main.services import find_school_and_allow_user, get_director, get_bookkeeper, get_updater, get_zavhoz


class PersonalOfSchoolInfo(APIView):
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
        director = get_director(school)
        bookkeeper = get_bookkeeper(school)
        responsible_for_filling = get_updater(school)
        zavhoz = get_zavhoz(school)
        ans = {}
        ans.update({get_model_name(director): PersonalAllInfoSerializer(director, many=False).data})
        ans.update({get_model_name(zavhoz): PersonalAllInfoSerializer(zavhoz, many=False).data})
        ans.update({get_model_name(bookkeeper): PersonalAllInfoSerializer(bookkeeper, many=False).data})
        ans.update({get_model_name(responsible_for_filling): PersonalAllInfoSerializer(responsible_for_filling,
                                                                                       many=False).data})
        return Response(data=ans)

    def put(self, request):
        data = request.data
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        director = get_director(school)
        bookkeeper = get_bookkeeper(school)
        responsible_for_filling = get_updater(school)
        zavhoz = get_zavhoz(school)
        try:
            director.update(data[get_model_name(director)])
            zavhoz.update(data.pop(get_model_name(zavhoz)))
            bookkeeper.update(data.pop(get_model_name(bookkeeper)))
            responsible_for_filling.update(data.pop(get_model_name(responsible_for_filling)))
        except BaseException as ex:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})

        return Response(status=status.HTTP_200_OK)
