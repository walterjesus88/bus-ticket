#Django Serializers
from rest_framework import serializers

#Models
from users.models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'         
        )

class UserSignUpSerializer(serializers.Serializer):
    email=serializers.EmailField()
    username=serializers.CharField(min_length=4,max_length=20)
    #phone_number = serializers.CharField()
    password=serializers.CharField(min_length=8,max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)
    
    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def create(self,data):
        data.pop('password_confirmation')
        user=User.objects.create_user(**data)
        print(user)
        return user