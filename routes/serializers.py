from rest_framework import serializers
from routes.models import Route, City


class RouteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = (
            'pk',
            'name',
        )


class RouteSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, data):
        route = Route.objects.create(**data)
        return route


class CityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'pk',
            'name'
        )


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, data):
        city = City.objects.create(**data)
        return city
