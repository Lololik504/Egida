from urllib.request import Request

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.backends import MyAuthentication
from accounts.services import get_user_class, SchoolAllInfoSerializer, DistrictsSerializer, MyUser, DistrictUser
from main.allows import school_allow, departament_allow
from main.models import School, Building, District
from main.serializers import SchoolInfoSerializer


class CreateBuilding(APIView):
    def post(self, request):
        data = request
        INN = data['INN']
        user_token = MyAuthentication.authenticate(MyAuthentication(), request)
        user = user_token[0]
        user = get_user_class(user)
        try:
            school = School.objects.get(INN=INN)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Cant find school with this INN'})
        if not school_allow(user, school):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        building = Building.objects.create(data)
        building.save()
        return Response(status=status.HTTP_200_OK)


class SchoolInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = request.headers
        INN = data['INN']
        user_token = MyAuthentication.authenticate(MyAuthentication(), request)
        user = user_token[0]
        user = get_user_class(user)
        try:
            school = School.objects.get(INN=INN)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Cant find school with this INN'})
        if not school_allow(user, school):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        school_serializer = SchoolAllInfoSerializer(school, many=False)
        return Response({'school': school_serializer.data})

    def put(self, request):
        data: dict = request.data
        INN = data['INN']
        user_token = MyAuthentication.authenticate(MyAuthentication(), request)
        user = user_token[0]
        user = get_user_class(user)
        try:
            school = School.objects.get(INN=INN)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Cant find school with this INN'})
        if not school_allow(user, school):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})
        try:
            if "Inn" in data:
                data.pop("Inn")
            for k, v in data.items():
                setattr(school, k, v)
            school.save()
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={'detail': 'Error with update method'})
        return Response(status=status.HTTP_200_OK)


class DistrictsInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user_token = MyAuthentication.authenticate(MyAuthentication(), request)
        user = user_token[0]
        user = get_user_class(user)
        if departament_allow(user):
            districts = District.objects.all()
            schools = School.objects.all()
            ans = []
            for district in districts:
                dist_schools = list(filter(lambda school: school.district == district, schools))
                ans.append( {
                    'name' : DistrictsSerializer(district, many=False).data,
                    'schools': SchoolInfoSerializer(dist_schools, many=True).data
                })

            return Response(ans)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                            data={'detail': 'You dont have permission to do this'})


class OneDistrictInfo(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: Request):
        user_token = MyAuthentication.authenticate(MyAuthentication(), request)
        user = user_token[0]
        user = get_user_class(user)
        district_name = request.headers['district']
        if user.permission <= MyUser.Permissions.district.value:
            try:
                if isinstance(user, DistrictUser):
                    district = user.district
                    if district_name != district.name:
                        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                                        data={'detail': 'You dont have permission to do this'})
                else:
                    district = District.objects.get(name=district_name)
                schools = School.objects.get(district=district)
                district_serializer = DistrictsSerializer(district, many=False)
                schools_serializer = SchoolInfoSerializer(schools, many=True)
                ans = {
                    'district': district_serializer.data,
                    'schools': schools_serializer.data
                }
                return Response(ans)
            except:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
