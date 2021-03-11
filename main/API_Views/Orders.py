from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from loguru import logger
from main.services import find_school_and_allow_user
from main.serializers.serializers import RospotrebSerializer, GospozhSerializer,\
    RostechSerializer, SudebSerializer, OtherOrdersSerializer
import datetime


class RospotrebView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
            rospotreb = school.rospotreb_set.get_or_create()[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        rospotreb_serializer = RospotrebSerializer(rospotreb)
        return Response({'rospotreb': rospotreb_serializer.data})

    def post(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        date_order = data.get('date-order')
        type_work = data.get('type-work')
        period_execution = data.get('period-execution')
        vkluchenie = data.get('vkluchenie')
        executed = data.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            school = find_school_and_allow_user(INN, user)
            rospotreb = school.rospotreb_set.get_or_create()[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            if date_order:
                date_order = datetime.datetime.strptime(date_order, '%d.%m.%Y').strftime('%Y-%m-%d')
            if period_execution:
                period_execution = datetime.datetime.strptime(period_execution, '%d.%m.%Y').strftime('%Y-%m-%d')
            rospotreb.date_order=date_order
            rospotreb.type_work=type_work
            rospotreb.period_execution=period_execution
            rospotreb.vkluchenie=vkluchenie
            rospotreb.executed=executed
            rospotreb.order=order
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
        field_id = None
        try:
            field_id = data['field-id']
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            school = find_school_and_allow_user(INN, user)
            rospotreb = school.rospotreb_set.get()
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        if field_id == 'date-order':
            rospotreb.date_order = None
        elif field_id == 'type-work':
            rospotreb.type_work = None
        elif field_id == 'period-execution':
            rospotreb.period_execution = None
        elif field_id == 'order':
            rospotreb.order.delete()
        elif field_id == 'vkluchenie':
            rospotreb.vkluchenie = None
        elif field_id == 'executed':
            rospotreb.executed = None
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": "No such field_id"})
        rospotreb.save()
        return Response(status=status.HTTP_200_OK)



class GospozhView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
            gospozh = school.gospozh_set.get_or_create()[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        gospozh_serializer = GospozhSerializer(gospozh)
        return Response({'gospozh': gospozh_serializer.data})

    def post(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        date_order = data.get('date-order')
        type_work = data.get('type-work')
        period_execution = data.get('period-execution')
        vkluchenie = data.get('vkluchenie')
        executed = data.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            school = find_school_and_allow_user(INN, user)
            gospozh = school.gospozh_set.get_or_create()[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            if date_order:
                date_order = datetime.datetime.strptime(date_order, '%d.%m.%Y').strftime('%Y-%m-%d')
            if period_execution:
                period_execution = datetime.datetime.strptime(period_execution, '%d.%m.%Y').strftime('%Y-%m-%d')
            gospozh.date_order=date_order
            gospozh.type_work=type_work
            gospozh.period_execution=period_execution
            gospozh.vkluchenie=vkluchenie
            gospozh.executed=executed
            gospozh.order=order
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
        field_id = None
        try:
            field_id = data['field-id']
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            school = find_school_and_allow_user(INN, user)
            gospozh = school.gospozh_set.get()
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        if field_id == 'date-order':
            gospozh.date_order = None
        elif field_id == 'type-work':
            gospozh.type_work = None
        elif field_id == 'period-execution':
            gospozh.period_execution = None
        elif field_id == 'order':
            gospozh.order.delete()
        elif field_id == 'vkluchenie':
            gospozh.vkluchenie = None
        elif field_id == 'executed':
            gospozh.executed = None
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": "No such field_id"})
        gospozh.save()
        return Response(status=status.HTTP_200_OK)


class RostechView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
            rostech = school.rostech_set.get_or_create()[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        rostech_serializer = RostechSerializer(rostech)
        return Response({'rostech': rostech_serializer.data})

    def post(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        date_order = data.get('date-order')
        type_work = data.get('type-work')
        period_execution = data.get('period-execution')
        vkluchenie = data.get('vkluchenie')
        executed = data.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            school = find_school_and_allow_user(INN, user)
            rostech = school.rostech_set.get_or_create()[0]
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
        field_id = None
        try:
            field_id = data['field-id']
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            school = find_school_and_allow_user(INN, user)
            rostech = school.rostech_set.get()
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        if field_id == 'date-order':
            rostech.date_order = None
        elif field_id == 'type-work':
            rostech.type_work = None
        elif field_id == 'period-execution':
            rostech.period_execution = None
        elif field_id == 'order':
            rostech.order.delete()
        elif field_id == 'vkluchenie':
            rostech.vkluchenie = None
        elif field_id == 'executed':
            rostech.executed = None
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": "No such field_id"})
        rostech.save()
        return Response(status=status.HTTP_200_OK)


class SudebView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
            sudeb = school.sudeb_set.get_or_create()[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        sudeb_serializer = SudebSerializer(sudeb)
        return Response({'sudeb': sudeb_serializer.data})

    def post(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        date_order = data.get('date-order')
        type_work = data.get('type-work')
        period_execution = data.get('period-execution')
        vkluchenie = data.get('vkluchenie')
        executed = data.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            school = find_school_and_allow_user(INN, user)
            sudeb = school.sudeb_set.get_or_create()[0]
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
        field_id = None
        try:
            field_id = data['field-id']
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            school = find_school_and_allow_user(INN, user)
            sudeb = school.sudeb_set.get()
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        if field_id == 'date-order':
            sudeb.date_order = None
        elif field_id == 'type-work':
            sudeb.type_work = None
        elif field_id == 'period-execution':
            sudeb.period_execution = None
        elif field_id == 'order':
            sudeb.order.delete()
        elif field_id == 'vkluchenie':
            sudeb.vkluchenie = None
        elif field_id == 'executed':
            sudeb.executed = None
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": "No such field_id"})
        sudeb.save()
        return Response(status=status.HTTP_200_OK)


class OtherOrdersView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        try:
            school = find_school_and_allow_user(INN, user)
            otherorders = school.otherorders_set.get_or_create()[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        otherorders_serializer = OtherOrdersSerializer(otherorders)
        return Response({'otherorders': otherorders_serializer.data})

    def post(self, request, *args, **kwargs):
        data = request.headers
        INN = data['INN']
        user = request.my_user
        date_order = data.get('date-order')
        type_work = data.get('type-work')
        period_execution = data.get('period-execution')
        vkluchenie = data.get('vkluchenie')
        executed = data.get('executed')
        order = None
        if request.FILES:
            order = request.FILES['file']
        try:
            school = find_school_and_allow_user(INN, user)
            otherorders = school.otherorders_set.get_or_create()[0]
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
        field_id = None
        try:
            field_id = data['field-id']
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        try:
            school = find_school_and_allow_user(INN, user)
            otherorders = school.otherorders_set.get()
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        if field_id == 'date-order':
            otherorders.date_order = None
        elif field_id == 'type-work':
            otherorders.type_work = None
        elif field_id == 'period-execution':
            otherorders.period_execution = None
        elif field_id == 'order':
            otherorders.order.delete()
        elif field_id == 'vkluchenie':
            otherorders.vkluchenie = None
        elif field_id == 'executed':
            otherorders.executed = None
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": "No such field_id"})
        otherorders.save()
        return Response(status=status.HTTP_200_OK)