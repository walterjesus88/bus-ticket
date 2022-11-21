from django.shortcuts import render

#Django rest framework
from rest_framework import mixins,status,viewsets
from rest_framework.response import Response
# Create your views here.
from vehicles.serializers import VehicleModelSerializer,VehicleSerializer

from vehicles.models import Vehicle
from users.models import User
from users.serializers.users import UserModelSerializer
#Permissions
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.decorators import action

class VehicleViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    
    queryset = Vehicle.objects.all()
    serializer_class= VehicleModelSerializer
    #lookup_field = 'name'
    

    def get_permissions(self):
        """Assign permissions based on action."""

        if self.action in ['Create', 'update']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    #@action(detail=False, methods=['post'])
    def create(self,request,*args,**kwargs):
        serializer=VehicleModelSerializer(data=request.data)


        serializer.is_valid(raise_exception=True)        
        vehicle = serializer.save()

        obj = User.objects.get(username="wjesus88")
        vehicle.passengers.add(obj)
        UserModelSerializer(vehicle)
       
        data = VehicleModelSerializer(vehicle).data
        return Response(data, status=status.HTTP_200_OK)



  