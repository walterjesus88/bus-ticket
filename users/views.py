from django.shortcuts import render

# Create your views here.

#Django rest framework
from rest_framework import mixins,status,viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
#Serializers
from users.serializers import (UserModelSerializer,UserSignUpSerializer,UserLoginSerializer,AccountVerificationSerializer)

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """ User view set """
    
    @action(detail=False,methods=['post'])
    def signup(self,request):
        """User signup"""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()      
        data= UserModelSerializer(user).data      
        #import pdb; pdb.set_trace()
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False,methods=['post'])
    def login(self,request):
        """User sign in"""
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()       
        data = {
            'user':UserModelSerializer(user).data,
            'access_token':token
        }
        return Response(data,status=status.HTTP_201_CREATED)

    @action(detail=False,methods=['post'])
    def verify(self,request):
        """Account verification"""
        serializer=AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data={'message':'congratulations!'}
        return Response(data,status=status.HTTP_200_OK)

