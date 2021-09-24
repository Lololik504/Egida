from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from main.serializers.serializers import ZPPPSerializer
from main.services import find_school_and_allow_user
from loguru import logger


class ZPPPView(APIView):
    permission_classes = [permissions.AllowAny]


    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        get_all = data.get('get_all')
        if get_all:
            try:
                school = find_school_and_allow_user(INN, user)
                zppp = school.zppp_set.select_related()
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            res = [ZPPPSerializer(i).data for i in zppp]
            return Response({'zppp': res})
        else:
            try:
                zppp_id = int(data['zppp-id'])
                school = find_school_and_allow_user(INN, user)
                zppp = school.zppp_set.get_or_create(id=zppp_id)[0]
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            res = ZPPPSerializer(zppp)
            return Response({'zppp': res.data})


    def put(self, request, *args, **kwargs):
        data: dict = request.headers
        data1: dict = request.data
        INN = data['INN']
        user = request.my_user
        try:
            zppp_id = data.get('zppp-id')
            school = find_school_and_allow_user(INN, user)
            if zppp_id:
                zppp_id = int(zppp_id)
                zppp = school.zppp_set.get_or_create(id=zppp_id)[0]
            else:
                zppp = school.zppp_set.create()[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        zppp.update(data1)
        zppp.save()
        return Response(status=status.HTTP_200_OK)



    def post(self, request, *args, **kwargs):
        data: dict = request.headers
        data1: dict = request.data
        INN = data['INN']
        user = request.my_user
        try:
            zppp_id = data.get('zppp-id')
            school = find_school_and_allow_user(INN, user)
            zppp = school.zppp_set.create()
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        zppp.update(data1)
        zppp.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        data: dict = request.headers
        data1: dict = request.data
        INN = data['INN']
        user = request.my_user
        try:
            zppp_id = data.get('zppp-id')
            school = find_school_and_allow_user(INN, user)
            zppp = school.zppp_set.get_or_create(id=zppp_id)[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        zppp.delete()
        return Response(status=status.HTTP_200_OK)