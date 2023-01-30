from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from routes.serializers import (RouteSerializer, RouteModelSerializer, CitySerializer, CityModelSerializer)
from routes.models import Route, City, Stopping
#Permissions
from rest_framework.permissions import (AllowAny, IsAuthenticated)

class RouteViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = RouteModelSerializer

    def get_permissions(self):
        """Assign permissions based on action."""

        if self.action in ['Create', 'update']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

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

    def get_permissions(self):
        """Assign permissions based on action."""

        if self.action in ['Create', 'update']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

class DemoViewSet(viewsets.GenericViewSet):
    def list(self, request):
        # data_route = {
        #     "name": "Cerro de Pasco - Lima"
        # }
        # data_city = {
        #     "name": "Ninacaca"
        # }
        #
        # serializer_route = RouteSerializer(data=data_route, context={"request": self.request})
        # serializer_route.is_valid(raise_exception=True)
        # route = serializer_route.save()
        #
        # serializer_city = CitySerializer(data=data_city, context={"request": self.request})
        # serializer_city.is_valid(raise_exception=True)
        # city = serializer_city.save()
        # route = Route.objects.create(name="Cerro de Pasco - Lima")
        # city = City.objects.create(name="La Oroya")

        route = Route.objects.get(pk="7b2a4f64-6a9f-46e5-9a88-590bb1fd6a2c")
        city = City.objects.get(pk="f749d1e4-1d5f-4a05-a4b7-ce662ab12778")

        Stopping.objects.create(route=route, city=city, has_agency=True)

        # return Response(data, status=status.HTTP_201_CREATED)

        return Response({"message": "Hello world!"}, status=status.HTTP_200_OK)


