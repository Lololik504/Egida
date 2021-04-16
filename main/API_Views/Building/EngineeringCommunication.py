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
        if  data.get('ground_loop'):
            data: dict = data.dict()
            data['ground_loop'] = True if data['ground_loop'] == 'true' else False if data['ground_loop'] == 'false' else None
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

    def delete(self, request):
        data = request.headers
        building_id = data['id']
        user = request.my_user
        doc_id = data['doc_id']
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
        if doc_id == 'technical_condition_of_the_heating_system_act':
            eng_communication.technical_condition_of_the_heating_system_act.delete()
        elif doc_id == 'technical_condition_of_the_ventilation_system_act':
            eng_communication.technical_condition_of_the_ventilation_system_act.delete()
        elif doc_id == 'technical_condition_of_the_hot_water_supply_system_act':
            eng_communication.technical_condition_of_the_hot_water_supply_system_act.delete()
        elif doc_id == 'passport_vvoda':
            eng_communication.passport_vvoda.delete()
        elif doc_id == 'schema_vvoda':
            eng_communication.schema_vvoda.delete()
        elif doc_id == 'passport_itp':
            eng_communication.passport_itp.delete()
        elif doc_id == 'schema_itp':
            eng_communication.schema_itp.delete()
        elif doc_id == 'act_balance_razgranich':
            eng_communication.act_balance_razgranich.delete()
        elif doc_id == 'schema_balance_razgranich':
            eng_communication.schema_balance_razgranich.delete()
        elif doc_id == 'spravka_teplov_nagruz':
            eng_communication.spravka_teplov_nagruz.delete()
        elif doc_id == 'raschet_teplov_poter':
            eng_communication.raschet_teplov_poter.delete()
        elif doc_id == 'toposnova':
            eng_communication.toposnova.delete()
        elif doc_id == 'technical_condition_of_the_internal_power_supply_system_act':
            eng_communication.technical_condition_of_the_internal_power_supply_system_act.delete()
        elif doc_id == 'technical_condition_of_the_external_power_supply_system_act':
            eng_communication.technical_condition_of_the_external_power_supply_system_act.delete()
        elif doc_id == 'power_supply_system_act_balance_razgranich':
            eng_communication.power_supply_system_act_balance_razgranich.delete()
        elif doc_id == 'power_supply_system_scheme_balance_razgranich':
            eng_communication.power_supply_system_scheme_balance_razgranich.delete()
        elif doc_id == 'power_supply_system_odnolinein_schema':
            eng_communication.power_supply_system_odnolinein_schema.delete()
        elif doc_id == 'power_supply_system_photo_vru':
            eng_communication.power_supply_system_photo_vru.delete()
        elif doc_id == 'technical_condition_of_the_water_supply_system_act':
            eng_communication.technical_condition_of_the_water_supply_system_act.delete()
        elif doc_id == 'technical_condition_of_the_sewerage_system_act':
            eng_communication.technical_condition_of_the_sewerage_system_act.delete()
        elif doc_id == 'water_supply_scheme_balance_razgranich':
            eng_communication.water_supply_scheme_balance_razgranich.delete()
        elif doc_id == 'water_supply_act_balance_razgranich':
            eng_communication.water_supply_act_balance_razgranich.delete()
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": "No such doc_id"})
        eng_communication.save()
        return Response(status=status.HTTP_200_OK)