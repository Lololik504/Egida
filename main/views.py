from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers.serializers import *
from .models import Building
from .models.building_construction import BuildingConstruction
from .serializers.building_construction_serializer import BuildingConstructionSerializer


def index(request):
    districts = District.objects.all()
    urls = []
    for district in districts:
        urls.append(district.name)
    context = {
        'districts': districts,
        'urls': urls
    }
    return render(request, 'main/index.html', context)


class TEST(APIView):

    def get(self, request):
        print("TEST")
        b = Building.objects.get(id=4)
        b_c = BuildingConstruction.objects.get_or_create(building=b)
        ans = BuildingConstructionSerializer(b_c).data
        print(ans)
        return Response(status=status.HTTP_200_OK)
