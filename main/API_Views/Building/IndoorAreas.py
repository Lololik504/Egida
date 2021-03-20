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
                          'gym_exhaust_ventilation', 'gym_exhaust_ventilation_is_workable', 'gym_supply_ventilation',
                          'gym_supply_ventilation_is_workable', 'auditorium_exhaust_ventilation',
                          'auditorium_exhaust_ventilation_is_workable', 'auditorium_supply_ventilation',
                          'auditorium_supply_ventilation_is_workable', 'bathroom_exhaust_ventilation',
                          'bathroom_exhaust_ventilation_is_workable', 'laundry_exhaust_ventilation',
                          'laundry_exhaust_ventilation_is_workable', 'auto_opening_of_emergency_exits_system']
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
