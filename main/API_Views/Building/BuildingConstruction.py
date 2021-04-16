from loguru import logger
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.building_construction import BuildingConstruction
from main.services import find_building_and_allow_user
from main.serializers.building_construction_serializer import *


class BuildingConstructionAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        building_id = data['id']
        user = request.my_user
        try:
            building = find_building_and_allow_user(building_id, user)
            building_constr = BuildingConstruction.objects.get_or_create(building=building)
            if building_constr[1]:
                building.building_construction = building_constr[0]
                building.save()
            building_constr = building_constr[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        ans = [BuildingConstructionSerializer(building_constr, many=False).data]
        return Response(status=status.HTTP_200_OK, data=ans)

    def put(self, request):
        data = request.data
        building_id = data['id']
        user = request.my_user
        if request.FILES:
            files = request.FILES
            data.update(files)
        try:
            building = find_building_and_allow_user(id=building_id, user=user)
            building_constr = BuildingConstruction.objects.get_or_create(building=building)
            if building_constr[1]:
                building.building_construction = building_constr[0]
                building.save()
            building_constr = building_constr[0]
            building_constr.update(data=data)
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        data = request.data
        building_id = data['id']
        user = request.my_user
        doc_id = data['doc_id']
        try:
            building = find_building_and_allow_user(building_id, user)
            building_constr = BuildingConstruction.objects.get_or_create(building=building)
            if building_constr[1]:
                building.building_construction = building_constr[0]
                building.save()
            building_constr = building_constr[0]
        except BaseException as ex:
            logger.exception(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": ex.__str__()})
        if doc_id == 'blind_area_act':
            building_constr.blind_area_act.delete()
        elif doc_id == 'blind_area_photo':
            building_constr.blind_area_photo.delete()
        elif doc_id == 'facade_photo':
            building_constr.facade_photo.delete()
        elif doc_id == 'facade_act':
            building_constr.facade_act.delete()
        elif doc_id == 'attic_overlapping_act':
            building_constr.attic_overlapping_act.delete()
        elif doc_id == 'basement_overlapping_act':
            building_constr.basement_overlapping_act.delete()
        elif doc_id == 'roof_photo':
            building_constr.roof_photo.delete()
        elif doc_id == 'roof_act':
            building_constr.roof_act.delete()
        elif doc_id == 'window_act':
            building_constr.window_act.delete()
        elif doc_id == 'foundation_photo':
            building_constr.foundation_photo.delete()
        elif doc_id == 'foundation_act':
            building_constr.foundation_act.delete()
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"detail": "No such doc_id"})
        building_constr.save()
        return Response(status=status.HTTP_200_OK)
