from rest_framework import serializers
from routes.models import Route, City, Stopping


class RouteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = (
            'pk',
            'name',
            'created_at',
            'updated_at',
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
            'name',
            'created_at',
            'updated_at',
        )


class StoppingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stopping
        fields = (
            'pk',
            'routes',
            'cities',
            'has_agency',
        )


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    # stoppings = StoppingModelSerializer(many=True)

    def create(self, data):
        city = City.objects.create(**data)
        return city


class StoppingSerializer(serializers.Serializer):
    routes = RouteModelSerializer(many=True)
    cities = CityModelSerializer(many=True)
    has_agency = serializers.CharField(max_length=255)
