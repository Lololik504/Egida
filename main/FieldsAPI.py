from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models.PersonalModel import Director, ZavHoz, Bookkeeper, Updater
from .models.services import get_model_fields
from main.serializers.serializers import *

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
