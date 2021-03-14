import json

from django.http import QueryDict
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from loguru import logger
from main.services import find_school_and_allow_user
from main.serializers.serializers import RospotrebSerializer, GospozhSerializer, \
    RostechSerializer, SudebSerializer, OtherOrdersSerializer
import datetime


class RospotrebView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        get_all = data.get('get_all')
        if get_all:
            try:
                school = find_school_and_allow_user(INN, user)
                rospotreb = school.rospotreb_set.select_related()
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            res = [RospotrebSerializer(i).data for i in rospotreb]
            return Response({'rospotreb': res})
        else:
            try:
                order_id = int(data['order-id'])
                school = find_school_and_allow_user(INN, user)
                rospotreb = school.rospotreb_set.get_or_create(id=order_id)[0]
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            rospotreb_serializer = RospotrebSerializer(rospotreb)
            return Response({'rospotreb': rospotreb_serializer.data})

    def put(self, request, *args, **kwargs):
        data = request.headers
        data2 = request.data
        data2: dict = data2.dict()
        data2 = json.dumps(data2)
        data2 = json.loads(data2)
        INN = data['INN']
        user = request.my_user
        date_order = data2.get('date-order')
        type_work = data2.get('type-work')
        summa = data2.get('summa')
        period_execution = data2.get('period-execution')
        vkluchenie = data2.get('vkluchenie')
        executed = data2.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            rospotreb = school.rospotreb_set.get_or_create(id=order_id)[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            if date_order:
                date_order = datetime.datetime.strptime(date_order, '%d.%m.%Y').strftime('%Y-%m-%d')
            if period_execution:
                period_execution = datetime.datetime.strptime(period_execution, '%d.%m.%Y').strftime('%Y-%m-%d')
            rospotreb.date_order = date_order
            rospotreb.type_work = type_work
            rospotreb.period_execution = period_execution
            rospotreb.vkluchenie = vkluchenie
            rospotreb.executed = executed
            rospotreb.order = order
            rospotreb.summa = summa
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        rospotreb.save()
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.headers
        data2 = request.data
        data2: dict = data2.dict()
        data2 = json.dumps(data2)
        data2 = json.loads(data2)
        INN = data['INN']
        user = request.my_user
        date_order = data2.get('date-order')
        type_work = data2.get('type-work')
        summa = data2.get('summa')
        period_execution = data2.get('period-execution')
        vkluchenie = True if data2.get('vkluchenie') == 'true' else False
        executed = True if data2.get('executed') == 'true' else False
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            # order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            rospotreb = school.rospotreb_set.create()
            # rospotreb.school = school
            # rospotreb = school.rospotreb_set.get_or_create(id=order_id)[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            if date_order:
                date_order = datetime.datetime.strptime(date_order, '%d.%m.%Y').strftime('%Y-%m-%d')
            if period_execution:
                period_execution = datetime.datetime.strptime(period_execution, '%d.%m.%Y').strftime('%Y-%m-%d')
            rospotreb.date_order = date_order
            rospotreb.type_work = type_work
            rospotreb.period_execution = period_execution
            rospotreb.vkluchenie = vkluchenie
            rospotreb.executed = executed
            rospotreb.order = order
            rospotreb.summa = summa
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        rospotreb.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            rospotreb = school.rospotreb_set.get(id=order_id)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        rospotreb.delete()

        return Response(status=status.HTTP_200_OK)


class GospozhView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        get_all = data.get('get_all')
        if get_all:
            try:
                school = find_school_and_allow_user(INN, user)
                gospozh = school.gospozh_set.select_related()
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            res = [GospozhSerializer(i).data for i in gospozh]
            return Response({'gospozh': res})
        else:
            try:
                order_id = int(data['order-id'])
                school = find_school_and_allow_user(INN, user)
                gospozh = school.gospozh_set.get_or_create(id=order_id)[0]
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            gospozh_serializer = GospozhSerializer(gospozh)
            return Response({'gospozh': gospozh_serializer.data})

    def put(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        data2 = request.data
        data2: dict = data2.dict()
        data2 = json.dumps(data2)
        data2 = json.loads(data2)
        user = request.my_user
        date_order = data2.get('date-order')
        type_work = data2.get('type-work')
        summa = data2.get('summa')
        period_execution = data2.get('period-execution')
        vkluchenie = data2.get('vkluchenie')
        executed = data2.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            gospozh = school.gospozh_set.get_or_create(id=order_id)[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            if date_order:
                date_order = datetime.datetime.strptime(date_order, '%d.%m.%Y').strftime('%Y-%m-%d')
            if period_execution:
                period_execution = datetime.datetime.strptime(period_execution, '%d.%m.%Y').strftime('%Y-%m-%d')
            gospozh.date_order = date_order
            gospozh.type_work = type_work
            gospozh.period_execution = period_execution
            gospozh.vkluchenie = vkluchenie
            gospozh.executed = executed
            gospozh.order = order
            gospozh.summa = summa
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        gospozh.save()
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        data2 = request.data
        data2: dict = data2.dict()
        data2 = json.dumps(data2)
        data2 = json.loads(data2)
        user = request.my_user
        date_order = data2.get('date-order')
        type_work = data2.get('type-work')
        summa = data2.get('summa')
        period_execution = data2.get('period-execution')
        vkluchenie = data2.get('vkluchenie')
        executed = data2.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            # order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            gospozh = school.gospozh_set.create()
            # gospozh = school.gospozh_set.get_or_create(id=order_id)[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            if date_order:
                date_order = datetime.datetime.strptime(date_order, '%d.%m.%Y').strftime('%Y-%m-%d')
            if period_execution:
                period_execution = datetime.datetime.strptime(period_execution, '%d.%m.%Y').strftime('%Y-%m-%d')
            gospozh.date_order = date_order
            gospozh.type_work = type_work
            gospozh.period_execution = period_execution
            gospozh.vkluchenie = vkluchenie
            gospozh.executed = executed
            gospozh.order = order
            gospozh.summa = summa
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        gospozh.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            gospozh = school.gospozh_set.get(id=order_id)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        gospozh.delete()
        return Response(status=status.HTTP_200_OK)


class RostechView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        get_all = data.get('get_all')
        if get_all:
            try:
                school = find_school_and_allow_user(INN, user)
                rostech = school.rostech_set.select_related()
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            res = [RostechSerializer(i).data for i in rostech]
            return Response({'rostech': res})
        else:
            try:
                order_id = int(data['order-id'])
                school = find_school_and_allow_user(INN, user)
                rostech = school.rostech_set.get_or_create(id=order_id)[0]
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            rostech_serializer = RostechSerializer(rostech)
            return Response({'rostech': rostech_serializer.data})

    def put(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        data2 = request.data
        data2: dict = data2.dict()
        data2 = json.dumps(data2)
        data2 = json.loads(data2)
        user = request.my_user
        date_order = data2.get('date-order')
        type_work = data2.get('type-work')
        summa = data2.get('summa')
        period_execution = data2.get('period-execution')
        vkluchenie = data2.get('vkluchenie')
        executed = data2.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            rostech = school.rostech_set.get_or_create(id=order_id)[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            if date_order:
                date_order = datetime.datetime.strptime(date_order, '%d.%m.%Y').strftime('%Y-%m-%d')
            if period_execution:
                period_execution = datetime.datetime.strptime(period_execution, '%d.%m.%Y').strftime('%Y-%m-%d')
            rostech.date_order = date_order
            rostech.type_work = type_work
            rostech.period_execution = period_execution
            rostech.vkluchenie = vkluchenie
            rostech.executed = executed
            rostech.order = order
            rostech.summa = summa
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        rostech.save()
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        data2 = request.data
        data2: dict = data2.dict()
        data2 = json.dumps(data2)
        data2 = json.loads(data2)
        user = request.my_user
        date_order = data2.get('date-order')
        type_work = data2.get('type-work')
        summa = data2.get('summa')
        period_execution = data2.get('period-execution')
        vkluchenie = data2.get('vkluchenie')
        executed = data2.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            # order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            rostech = school.rostech_set.create()
            # rostech = school.rostech_set.get_or_create(id=order_id)[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            if date_order:
                date_order = datetime.datetime.strptime(date_order, '%d.%m.%Y').strftime('%Y-%m-%d')
            if period_execution:
                period_execution = datetime.datetime.strptime(period_execution, '%d.%m.%Y').strftime('%Y-%m-%d')
            rostech.date_order = date_order
            rostech.type_work = type_work
            rostech.period_execution = period_execution
            rostech.vkluchenie = vkluchenie
            rostech.executed = executed
            rostech.order = order
            rostech.summa = summa
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        rostech.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user

        try:
            order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            rostech = school.rostech_set.get(id=order_id)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})

        rostech.delete()
        return Response(status=status.HTTP_200_OK)


class SudebView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        get_all = data.get('get_all')
        if get_all:
            try:
                school = find_school_and_allow_user(INN, user)
                sudeb = school.sudeb_set.select_related()
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            res = [SudebSerializer(i).data for i in sudeb]
            return Response({'sudeb': res})
        else:
            try:
                order_id = int(data['order-id'])
                school = find_school_and_allow_user(INN, user)
                sudeb = school.sudeb_set.get_or_create(id=order_id)[0]
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            sudeb_serializer = SudebSerializer(sudeb)
            return Response({'sudeb': sudeb_serializer.data})

    def put(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        data2 = request.data
        data2: dict = data2.dict()
        data2 = json.dumps(data2)
        data2 = json.loads(data2)
        user = request.my_user
        date_order = data2.get('date-order')
        type_work = data2.get('type-work')
        summa = data2.get('summa')
        period_execution = data2.get('period-execution')
        vkluchenie = data2.get('vkluchenie')
        executed = data2.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            sudeb = school.sudeb_set.get_or_create(id=order_id)[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            if date_order:
                date_order = datetime.datetime.strptime(date_order, '%d.%m.%Y').strftime('%Y-%m-%d')
            if period_execution:
                period_execution = datetime.datetime.strptime(period_execution, '%d.%m.%Y').strftime('%Y-%m-%d')
            sudeb.date_order = date_order
            sudeb.type_work = type_work
            sudeb.period_execution = period_execution
            sudeb.vkluchenie = vkluchenie
            sudeb.executed = executed
            sudeb.order = order
            sudeb.summa = summa
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        sudeb.save()
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        data2 = request.data
        data2: dict = data2.dict()
        data2 = json.dumps(data2)
        data2 = json.loads(data2)
        user = request.my_user
        date_order = data2.get('date-order')
        type_work = data2.get('type-work')
        summa = data2.get('summa')
        period_execution = data2.get('period-execution')
        vkluchenie = data2.get('vkluchenie')
        executed = data2.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            # order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            sudeb = school.sudeb_set.create()
            # sudeb = school.sudeb_set.get_or_create(id=order_id)[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            if date_order:
                date_order = datetime.datetime.strptime(date_order, '%d.%m.%Y').strftime('%Y-%m-%d')
            if period_execution:
                period_execution = datetime.datetime.strptime(period_execution, '%d.%m.%Y').strftime('%Y-%m-%d')
            sudeb.date_order = date_order
            sudeb.type_work = type_work
            sudeb.period_execution = period_execution
            sudeb.vkluchenie = vkluchenie
            sudeb.executed = executed
            sudeb.order = order
            sudeb.summa = summa
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        sudeb.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            sudeb = school.sudeb_set.get(id=order_id)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        sudeb.delete()
        return Response(status=status.HTTP_200_OK)


class OtherOrdersView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        get_all = data.get('get_all')
        if get_all:
            try:
                school = find_school_and_allow_user(INN, user)
                otherorders = school.otherorders_set.select_related()
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            res = [OtherOrdersSerializer(i).data for i in otherorders]
            return Response({'otherorders': res})
        else:
            try:
                order_id = int(data['order-id'])
                school = find_school_and_allow_user(INN, user)
                otherorders = school.otherorders_set.get_or_create(id=order_id)[0]
            except BaseException as ex:
                logger.exception(ex)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})
            otherorders_serializer = OtherOrdersSerializer(otherorders)
            return Response({'otherorders': otherorders_serializer.data})

    def put(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        data2 = request.data
        data2: dict = data2.dict()
        data2 = json.dumps(data2)
        data2 = json.loads(data2)
        user = request.my_user
        date_order = data2.get('date-order')
        type_work = data2.get('type-work')
        summa = data2.get('summa')
        period_execution = data2.get('period-execution')
        vkluchenie = data2.get('vkluchenie')
        executed = data2.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            otherorders = school.otherorders_set.get_or_create(id=order_id)[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            if date_order:
                date_order = datetime.datetime.strptime(date_order, '%d.%m.%Y').strftime('%Y-%m-%d')
            if period_execution:
                period_execution = datetime.datetime.strptime(period_execution, '%d.%m.%Y').strftime('%Y-%m-%d')
            otherorders.date_order = date_order
            otherorders.type_work = type_work
            otherorders.period_execution = period_execution
            otherorders.vkluchenie = vkluchenie
            otherorders.executed = executed
            otherorders.order = order
            otherorders.summa = summa
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        otherorders.save()
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        data2 = request.data
        data2: dict = data2.dict()
        data2 = json.dumps(data2)
        data2 = json.loads(data2)
        user = request.my_user
        date_order = data2.get('date-order')
        type_work = data2.get('type-work')
        summa = data2.get('summa')
        period_execution = data2.get('period-execution')
        vkluchenie = data2.get('vkluchenie')
        executed = data2.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            # order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            otherorders = school.otherorders_set.create()
            # otherorders = school.otherorders_set.get_or_create(id=order_id)[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            if date_order:
                date_order = datetime.datetime.strptime(date_order, '%d.%m.%Y').strftime('%Y-%m-%d')
            if period_execution:
                period_execution = datetime.datetime.strptime(period_execution, '%d.%m.%Y').strftime('%Y-%m-%d')
            otherorders.date_order = date_order
            otherorders.type_work = type_work
            otherorders.period_execution = period_execution
            otherorders.vkluchenie = vkluchenie
            otherorders.executed = executed
            otherorders.order = order
            otherorders.summa = summa
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        otherorders.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            order_id = int(data['order-id'])
            school = find_school_and_allow_user(INN, user)
            otherorders = school.otherorders_set.get(id=order_id)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        otherorders.delete()
        return Response(status=status.HTTP_200_OK)
