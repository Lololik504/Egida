from rest_framework.serializers import ModelSerializer

from main.models import District, School


class DistrictsSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name']


class SchoolsSerializer(ModelSerializer):
    # Сериализация ForeignKey
    district = DistrictsSerializer()

    class Meta:
        model = School
        fields = ['name', 'shortname', 'phone', 'district']


