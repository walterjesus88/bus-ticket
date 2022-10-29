from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from routes.serializers import (RouteSerializer, RouteModelSerializer, CitySerializer, CityModelSerializer)
from routes.models import Route, City


class RouteViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = RouteModelSerializer

    def get_queryset(self):
        queryset = Route.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = RouteSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        route = serializer.save()
        data = RouteModelSerializer(route).data
        return Response(data, status=status.HTTP_201_CREATED)


class CityViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = CityModelSerializer

    def get_queryset(self):
        queryset = City.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = CitySerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        city = serializer.save()
        data = CityModelSerializer(city).data
        return Response(data, status=status.HTTP_201_CREATED)

