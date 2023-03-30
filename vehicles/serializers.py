#Import serializers
from rest_framework import serializers

#Models
from vehicles.models import Vehicle
from users.models import User
from routes.models import Route

from users.serializers.users import UserModelSerializer
from routes.serializers import  RouteModelSerializer,RouteSerializer
#.serializers #import UserModelSerializer
from rest_framework.fields import SerializerMethodField

class VehicleModelSerializer(serializers.ModelSerializer):
    
    route = RouteModelSerializer(read_only=True)

    #route = serializers.PrimaryKeyRelatedField(queryset=Route.objects.all(),many=False)

    #passengers = UserModelSerializer(many=True, read_only=True)
    #passengers = serializers.PrimaryKeyRelatedField(many=True,queryset=User.objects.all())
    #print('passengers-------------------------vvhgffgjvvvvvvvvvvvvvvvvvvvv--------------------')
    #print(dir(passengers))
    #print(passengers.get_value)
    #import pdb; pdb.set_trace()

    class Meta:
        model = Vehicle
        fields = '__all__'

import json
class VehicleDetailSerializer(serializers.ModelSerializer):
    routes = RouteModelSerializer(source='route')
  
    class Meta:
        model = Vehicle
        #fields = '__all__'
        fields = ('name', 'license', 'available_seats', 'description','routes')

class VehicleSerializer(serializers.Serializer):
    #route = RouteModelSerializer(read_only=False)
    
    name = serializers.CharField(max_length=255)
    license = serializers.CharField(max_length=255)    
    available_seats = serializers.IntegerField()
    description = serializers.CharField(max_length=255)
    #sroute = serializers.PrimaryKeyRelatedField(queryset=Route.objects.all(),many=False)

    print('estoy en vehicleserializer')
    
    def create(self,data):
        Vehicles = Vehicle.objects.create(**data)
        return Vehicles

    # def update(self, instance, validated_data):
    #     print('estoy en update')
    #     print(instance.route)
    #     print(instance)
    #     print(validated_data)
    #     instance.route = validated_data.get('route', instance.route)
    #     instance.license = validated_data.get('license', instance.license)
    #     instance.save()
    #     return instance

    def update(self, instance, validated_data) -> Vehicle:
        print('estoy en update')
        print(instance)
        for attr,value in self.validated_data.items():
            setattr(self.instance,attr,value)
        
        self.instance.save()
        return self.instance
