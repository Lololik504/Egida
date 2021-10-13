from loguru import logger
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.indoor_areas import IndoorAreas
from main.serializers.indoor_areas_serializer import IndoorAreasSerializer
from main.services import find_building_and_allow_user


def find_and_change_bool_vars(data):
    change_dict = False
    array_of_bool_vars = ['food_block_exhaust_ventilation', 'food_block_exhaust_ventilation_is_workable',
                          'food_block_supply_ventilation', 'food_block_supply_ventilation_is_workable',
                          'food_block_equipment_cost', 'food_block_combine_availability',
                          'food_block_dining_availability',
                          'food_block_production_availability',
                          'gym_exhaust_ventilation', 'gym_exhaust_ventilation_is_workable', 'gym_supply_ventilation',
                          'gym_supply_ventilation_is_workable', 'auditorium_exhaust_ventilation',
                          'auditorium_exhaust_ventilation_is_workable', 'auditorium_supply_ventilation',
                          'auditorium_supply_ventilation_is_workable', 'bathroom_exhaust_ventilation',
                          'bathroom_exhaust_ventilation_is_workable', 'laundry_exhaust_ventilation',
                          'laundry_exhaust_ventilation_is_workable', 'auto_opening_of_emergency_exits_system',
                          'pool_available', 'pool_working', 'filtration_unit', 'laundry_supply_ventilation',
                         'laundry_supply_ventilation_is_workable', 'pool_exhaust_ventilation', 'pool_supply_ventilation']
    for key in array_of_bool_vars:
        if data.get(key):
            if not change_dict:
                data: dict = data.dict()
                change_dict = True
            data[key] = True if data[key] == 'true' else False if data[key] == 'false' else None
    return data


class IndoorAreasAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(building_id, user)
            ind_areas = IndoorAreas.objects.get_or_create(building=building)
            if ind_areas[1]:
                building.indoor_areas = ind_areas[0]
                building.save()
            ind_areas = ind_areas[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        ans = [IndoorAreasSerializer(ind_areas, many=False).data]
        return Response(status=status.HTTP_200_OK, data=ans)

    def put(self, request):
        data = request.data
        building_id = data['id']
        user = request.my_user
        if request.FILES:
            files = request.FILES
            data.update(files)
        data = find_and_change_bool_vars(data)
        try:
            building = find_building_and_allow_user(id=building_id, user=user)
            ind_areas = IndoorAreas.objects.get_or_create(building=building)
            if ind_areas[1]:
                building.indoor_areas = ind_areas[0]
                building.save()
            ind_areas = ind_areas[0]
            ind_areas.update(data=data)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        data = request.headers
        building_id = data['id']
        user = request.my_user
        doc_id = data['docId']
        try:
            building = find_building_and_allow_user(building_id, user)
            ind_areas = IndoorAreas.objects.get_or_create(building=building)
            if ind_areas[1]:
                building.indoor_areas = ind_areas[0]
                building.save()
            ind_areas = ind_areas[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        if doc_id == 'admin_room_act':
            ind_areas.admin_room_act.delete()
        elif doc_id == 'auditorium_act':
            ind_areas.auditorium_act.delete()
        elif doc_id == 'bathroom_act':
            ind_areas.bathroom_act.delete()
        elif doc_id == 'classroom_act':
            ind_areas.classroom_act.delete()
        elif doc_id == 'corridors_act':
            ind_areas.corridors_act.delete()
        elif doc_id == 'emergency_exit_act':
            ind_areas.emergency_exit_act.delete()
        elif doc_id == 'food_block_act':
            ind_areas.food_block_act.delete()
        elif doc_id == 'gym_act':
            ind_areas.gym_act.delete()
        elif doc_id == 'laundry_act':
            ind_areas.laundry_act.delete()
        elif doc_id == 'pantry_act':
            ind_areas.pantry_act.delete()
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": "No such doc_id"})
        ind_areas.save()
        return Response(status=status.HTTP_200_OK)
