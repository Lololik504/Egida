from django.shortcuts import render
from rest_framework import status, permissions
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
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        print("TEST")
        b = Building.objects.get_or_create(school_id=1)[0]
        # b_c = BuildingConstruction.objects.get_or_create(building=b.id)
        ans = BuildingSerializer(b, many=False).data
        print(ans)
        return Response(status=status.HTTP_200_OK, data=ans)
