#Django Serializers
from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import password_validation,authenticate
from users.serializers.profiles import ProfileModelSerializer
#from vehicles.serializers import VehicleModelSerializer
#Models
from users.models import User, Profile
from rest_framework.authtoken.models import Token

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from datetime import timedelta

# Utilities
import jwt
class UserModelSerializer(serializers.ModelSerializer):
    
    profile = ProfileModelSerializer(read_only=True)
    #vehicles = VehicleModelSerializer(many=True, read_only=True)
    class Meta:
        model= User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'profile',
            #'vehicles'      
        )
        #extra_kwargs = {'vehicles': {'required': False}}

class UserSignUpSerializer(serializers.Serializer):
    email=serializers.EmailField()
    username=serializers.CharField(min_length=4,max_length=20)
    phone_number = serializers.CharField()
    password=serializers.CharField(min_length=8,max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)
    
    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self,data):
        """Verify passwords match."""

        passw=data['password']
        passw_conf=data['password_confirmation']
        if passw != passw_conf:
            raise serializers.ValidationError('password not match!')
        password_validation.validate_password(passw)
        return data
   
    def create(self,data):
        data.pop('password_confirmation')
        user=User.objects.create_user(**data,is_verified=False,is_client=True)
    
        Profile.objects.create(user=user)
        self.send_confirmation_email(user)
        return user

    def gen_verification_token(self,user):
        exp_date=timezone.now()+timedelta(days=2)
        payload={
            'user': user.username,
            'exp': int(exp_date.timestamp()),
            'type': 'email_confirmation'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        #print(token)
        #import pdb; pdb.set_trace()
        return token.decode()

    def send_confirmation_email(self,user):
        verification_token=self.gen_verification_token(user)
        print(verification_token)
        # subject = 'Welcome @{}! Verify your account to start '.format(user.username)
        # from_email = 'Bus-Tickets <noreply@bustickets.com>'
        # content = render_to_string(
        #     'emails/users/account_verification.html',
        #     {'token': verification_token, 'user': user}
        # )
        # msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        # msg.attach_alternative(content, "text/html")
        # msg.send()

class UserLoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(min_length=8,max_length=64)

    def to_representation(self, instance):
        return {
            'id': 'prueba',
            
        }

    def validate(self,data):
        user=authenticate(username=data['email'],password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        
        if not user.is_verified:
            raise serializers.ValidationError('Account is not active')
        self.context['user']=user
        return data

    def create(self,data):
        """Generate or retrieve new token"""
        token, created =Token.objects.get_or_create(user=self.context['user'])
        
        print(token)
        print(created)
        #import pdb; pdb.set_trace()
        return self.context['user'],token.key
       

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # personalizar el valor de ejemplo para la respuesta
        return data

        
class AccountVerificationSerializer(serializers.Serializer):
    
    token = serializers.CharField()
    def validate_token(self,data):
        """Verify token is valid."""
     
        try:
            payload=jwt.decode(data,settings.SECRET_KEY,algorithms=['HS256'])      
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token')
    
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Invalid token')
        
        self.context['payload'] = payload
        return data

    def save(self):
        """update user verified status"""
       
        payload=self.context['payload']       
        #import pdb; pdb.set_trace()
        user=User.objects.get(username=payload['user'])
        user.is_verified=True
        user.save()

