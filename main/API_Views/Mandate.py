from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from main.serializers.serializers import MandateCouncilSerializer, MandateAssemblySerializer
from main.services import find_school_and_allow_user
from loguru import logger


class MandateCouncilView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        get_all = data.get('get_all')
        if get_all:
            try:
                school = find_school_and_allow_user(INN, user)
                mandates = school.mandatecouncil_set.select_related()
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            res = [MandateCouncilSerializer(i).data for i in mandates]
            return Response({'mandates': res})
        else:
            try:
                mandate_id = int(data['mandate-id'])
                school = find_school_and_allow_user(INN, user)
                mandate = school.mandatecouncil_set.get_or_create(id=mandate_id)[0]
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            mandate_serializer = MandateCouncilSerializer(mandate)
            return Response({'mandate': mandate_serializer.data})

    def put(self, request, *args, **kwargs):
        data: dict = request.headers
        INN = data['INN']
        user = request.my_user
        file = None
        if request.FILES:
            file = request.FILES['file']
        data['file'] = file
        try:
            mandate_id = data.get('mandate-id')
            school = find_school_and_allow_user(INN, user)
            if mandate_id:
                mandate_id = int(data['mandate-id'])
                mandate = school.mandatecouncil_set.get_or_create(id=mandate_id)[0]
            else:
                mandate = school.mandatecouncil_set.create()[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        mandate.update(data)
        if file:
            mandate.file = file
        mandate.save()
        return Response(status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        data: dict = request.headers
        INN = data['INN']
        user = request.my_user
        file = None
        if request.FILES:
            file = request.FILES['file']
        data['file'] = file
        try:
            mandate_id = data.get('mandate-id')
            school = find_school_and_allow_user(INN, user)
            mandate = school.mandatecouncil_set.create()
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        mandate.update(data)
        if file:
            mandate.file = file
        mandate.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            mandate_id = int(data['mandate-id'])
            school = find_school_and_allow_user(INN, user)
            mandate = school.mandatecouncil_set.get(id=mandate_id)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        mandate.delete()
        return Response(status=status.HTTP_200_OK)


class MandateAssemblyView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        get_all = data.get('get_all')
        if get_all:
            try:
                school = find_school_and_allow_user(INN, user)
                mandates = school.mandateassembly_set.select_related()
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            res = [MandateAssemblySerializer(i).data for i in mandates]
            return Response({'mandates': res})
        else:
            try:
                mandate_id = int(data['mandate-id'])
                school = find_school_and_allow_user(INN, user)
                mandate = school.mandateassembly_set.get_or_create(id=mandate_id)[0]
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            mandate_serializer = MandateAssemblySerializer(mandate)
            return Response({'mandate': mandate_serializer.data})

    def put(self, request, *args, **kwargs):
        data: dict = request.headers
        INN = data['INN']
        user = request.my_user
        file = None
        if request.FILES:
            file = request.FILES['file']
        data['file'] = file
        try:
            mandate_id = data.get('mandate-id')
            school = find_school_and_allow_user(INN, user)
            if mandate_id:
                mandate_id = int(data['mandate-id'])
                mandate = school.mandateassembly_set.get_or_create(id=mandate_id)[0]
            else:
                mandate = school.mandateassembly_set.create()[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        mandate.update(data)
        if file:
            mandate.file = file
        mandate.save()
        return Response(status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        data: dict = request.headers
        INN = data['INN']
        user = request.my_user
        file = None
        if request.FILES:
            file = request.FILES['file']
        data['file'] = file
        try:
            mandate_id = data.get('mandate-id')
            school = find_school_and_allow_user(INN, user)
            mandate = school.mandateassembly_set.create()
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        mandate.update(data)
        if file:
            mandate.file = file
        mandate.save()
        return Response(status=status.HTTP_200_OK)


    def delete(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            mandate_id = int(data['mandate-id'])
            school = find_school_and_allow_user(INN, user)
            mandate = school.mandateassembly_set.get(id=mandate_id)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        mandate.delete()
        return Response(status=status.HTTP_200_OK)
