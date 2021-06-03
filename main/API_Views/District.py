from loguru import logger
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.allows import departament_allow, district_allow
from main.models import District
from main.serializers.serializers import DistrictsSerializer, SchoolInfoSerializer


class DistrictsInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = request.my_user
        if district_allow(user, user.district):
            district = user.district
            dist_schools = district.school_set.all()
            ans = [{
                'name': DistrictsSerializer(district, many=False).data,
                'schools': SchoolInfoSerializer(dist_schools, many=True).data
            }]
            return Response(ans)
        elif departament_allow(user):
            districts = District.objects.all()
            ans = []
            for district in districts:
                dist_schools = district.school_set.all()
                ans.append({
                    'name': DistrictsSerializer(district, many=False).data,
                    'schools': SchoolInfoSerializer(dist_schools, many=True).data
                })
            logger.success(str.format("{0} Получил информацию о всех районах", user))
            return Response(ans)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})


class OneDistrictInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = request.my_user
        district_name = request.headers['district']
        try:
            district = District.objects.get(name=district_name)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Cant find district'})
        if district_allow(user, district):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        else:
            try:
                schools = district.school_set.all()
                district_serializer = DistrictsSerializer(district, many=False)
                schools_serializer = SchoolInfoSerializer(schools, many=True)
                ans = {
                    'district': district_serializer.data,
                    'schools': schools_serializer.data
                }
                logger.success(str.format("{0} Получил информацию о {1}", user, district))
                return Response(ans)
            except BaseException as ex:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={"detail": ex.__str__()})


class DistrictsQuery(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        districts = District.objects.all()
        ans = DistrictsSerializer(districts, many=True).data
        return Response(ans)
