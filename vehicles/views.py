from django.shortcuts import render

#Django rest framework
from rest_framework import mixins,status,viewsets
from rest_framework.response import Response
# Create your views here.
from vehicles.serializers import VehicleModelSerializer,VehicleSerializer
from routes.serializers import RouteModelSerializer

from vehicles.models import Vehicle
from users.models import User
from routes.models import Route
from users.serializers.users import UserModelSerializer
#Permissions
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.decorators import action
from rest_framework import filters



class VehicleViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,                   
                    viewsets.GenericViewSet):
    search_fields = ['description','name']
    filter_backends = (filters.SearchFilter,)
    queryset = Vehicle.objects.all()
    serializer_class= VehicleModelSerializer
    lookup_field = 'name'
    

    def get_permissions(self):
        """Assign permissions based on action."""

        if self.action in ['Create', 'update']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    #@action(detail=False, methods=['post'])
    # def create(self,request,*args,**kwargs):
    #     serializer=VehicleModelSerializer(data=request.data)

    #     serializer.is_valid(raise_exception=True)        
    #     vehicle = serializer.save()

    #     data = VehicleModelSerializer(vehicle).data
    #     return Response(data, status=status.HTTP_200_OK)


    @action(detail=True,methods=['get','post'])
    def passenger(self,request,*args,**kwargs):
        """"manytomany passengers"""
        vehicle = self.get_object()
        user=request.data
        print(user['passenger'])
        #import pdb; pdb.set_trace()
        
        obj = User.objects.get(username=user['passenger'])
        vehicle.passengers.add(obj)
        UserModelSerializer(vehicle)
    
        data = VehicleModelSerializer(vehicle).data
        return Response(data, status=status.HTTP_200_OK)
    
    @action(detail=True,methods=['post','patch'])
    def route(self,request,*args,**kwargs):
        # vehicle = self.get_object()
        route_id=request.data
        
        print('route_id')
        print(route_id['name'])
        
        obj = Route.objects.get(name=route_id['name'])
 
        vehicle = self.get_object()   

        route = vehicle.route
        
        vehicle.route= obj

        partial = request.method=='PATCH'
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(
            vehicle,
            data={'route': obj.id},
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = VehicleModelSerializer(vehicle).data
        return Response(data, status=status.HTTP_200_OK)
