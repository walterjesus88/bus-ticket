#Import serializers
from rest_framework import serializers
#Models
from vehicles.models import Vehicle
from users.models import User

from users.serializers.users import UserModelSerializer
#.serializers #import UserModelSerializer

class VehicleModelSerializer(serializers.ModelSerializer):
    
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
    
    name = serializers.CharField(max_length=255)
    license = serializers.CharField(max_length=255)
    
    available_seats = serializers.IntegerField()

    def create(self,data):
        Vehicles = Vehicle.objects.create(**data)
        return Vehicles


