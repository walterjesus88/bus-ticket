#Import serializers
from rest_framework import serializers

#Models
from vehicles.models import Vehicle
from users.models import User
from routes.models import Route

from users.serializers.users import UserModelSerializer
from routes.serializers import  RouteModelSerializer
#.serializers #import UserModelSerializer

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


class VehicleSerializer(serializers.Serializer):
    #route = RouteModelSerializer(read_only=False)
    
    name = serializers.CharField(max_length=255)
    license = serializers.CharField(max_length=255)
    
    available_seats = serializers.IntegerField()
    #sroute = serializers.PrimaryKeyRelatedField(queryset=Route.objects.all(),many=False)


    def create(self,data):
        Vehicles = Vehicle.objects.create(**data)
        return Vehicles

    def update(self, instance, validated_data):
        print('fdgdg')
        print(instance.route)
        instance.route = validated_data.get('route', instance.route)
        instance.save()
