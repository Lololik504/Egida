from loguru import logger
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import MyUser, SchoolUser
from main.allows import district_allow
from main.models import School
from main.serializers import SchoolAllInfoSerializer
from main.services import find_school_and_allow_user


class SchoolInfo(APIView):
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
        school_serializer = SchoolAllInfoSerializer(school, many=False)
        logger.success(str.format("{0} Получил информацию о {1}", user, school))
        return Response({'school': school_serializer.data})

    def put(self, request):
        data: dict = request.data
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            school.update(data)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': ex.__str__()})
        logger.success(str.format("{0} Обновил информацию о {1}", user, school))
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        data: dict = request.data
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        if user.permission > MyUser.Permissions.DISTRICT.value:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        try:
            school = School.create(**data)
            SchoolUser.objects.create(username=school.INN, password=school.INN, school=school)

        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': ex.__str__()})
        logger.success(str.format("{0} Добавил информацию о {1}", user, school))
        return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        data: dict = request.headers
        user = request.my_user
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'detail': 'You need to authorize'})
        if user.permission > MyUser.Permissions.DISTRICT.value:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        try:
            school = School.objects.get(INN=data['INN'])
            if not (district_allow(user, school.district)):
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                                data={'detail': 'You dont have permission to do this'})
            school.delete()
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': ex.__str__()})
        logger.success(str.format("{0} Удалил информацию о {1}", user, school))
        return Response(status=status.HTTP_200_OK)
