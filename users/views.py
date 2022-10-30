from django.shortcuts import render

# Create your views here.

#Django rest framework
from rest_framework import mixins,status,viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
#Serializers
from users.serializers import (UserModelSerializer,UserSignUpSerializer)

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
        return Response(data, status=status.HTTP_201_CREATED)
