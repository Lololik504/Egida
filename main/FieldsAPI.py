from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers.serializers import *
from .models.PersonalModel import Director, ZavHoz, Bookkeeper, Updater
from .models.building_construction import BuildingConstruction

from .models.engineering_communication import EngineeringCommunication
from .models.indoor_areas import IndoorAreas
from .models.safety_system import SafetySystem
from .models.services import get_model_fields
from .models.territory_improvement import TerritoryImprovement
from .models.sports_facilities import SportsFacilities
from .models.accessible_environment import AccessibleEnvironment

Models = [School, Building, Director, ZavHoz, Bookkeeper, Updater, Temperature]


class BuildingFields(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        ans = {}
        fields = get_model_fields(Building)
        for field in fields:
            ans.update({field.name: field.verbose_name})
        return Response(ans)


class SchoolFields(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        ans = {}
        fields = get_model_fields(School)
        for field in fields:
            ans.update({field.name: field.verbose_name})
        return Response(ans)


class DistrictFields(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        ans = {}
        fields = get_model_fields(District)
        for field in fields:
            ans.update({field.name: field.verbose_name})
        return Response(ans)


class DirectorFields(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        ans = {}
        fields = get_model_fields(Director)
        for field in fields:
            ans.update({field.name: field.verbose_name})
        return Response(ans)


class PersonalFields(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        ans = {}
        fields = get_model_fields(Personal)
        for field in fields:
            ans.update({field.name: field.verbose_name})
        return Response(ans)


class AllModels(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        ans = {}
        for model in Models:
            ans.update({model._meta.model_name: model._meta.verbose_name})
        return Response(ans)


class Filters(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        districts = District.objects.all()
        res = {}
        for dist in districts:
            res.update({dist.id.__str__(): dist.name})
        res = {District._meta.model_name: res}
        return Response(res)


class BuildingConstructionFields(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        fields = list(get_model_fields(BuildingConstruction))
        ans = []
        for f in fields:
            ans.append({f.name: f.verbose_name})
        return Response(data=ans)


class EngineeringCommunicationFields(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        fields = list(get_model_fields(EngineeringCommunication))
        ans = []
        for f in fields:
            ans.append({f.name: f.verbose_name})
        return Response(data=ans)


class IndoorAreasFields(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        fields = list(get_model_fields(IndoorAreas))
        ans = []
        for f in fields:
            ans.append({f.name: f.verbose_name})
        return Response(data=ans)


class SafetySystemFields(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        fields = list(get_model_fields(SafetySystem))
        ans = []
        for f in fields:
            ans.append({f.name: f.verbose_name})
        return Response(data=ans)


class TerritoryImprovementFields(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        fields = list(get_model_fields(TerritoryImprovement))
        ans = []
        for f in fields:
            ans.append({f.name: f.verbose_name})
        return Response(data=ans)


class SportsFacilitiesFields(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        fields = list(get_model_fields(SportsFacilities))
        ans = []
        for f in fields:
            ans.append({f.name: f.verbose_name})
        return Response(data=ans)


class AccessibleEnvironmentFields(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        fields = list(get_model_fields(AccessibleEnvironment))
        ans = []
        for f in fields:
            ans.append({f.name: f.verbose_name})
        return Response(data=ans)
