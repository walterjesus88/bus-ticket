#from django.shortcuts import render
from django.shortcuts import get_object_or_404,render
# Create your views here.

#Django rest framework
from rest_framework import mixins,status,viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

#Models
from users.models import User, Profile

#Permissions
from rest_framework.permissions import (AllowAny, IsAuthenticated)

#Serializers
from users.serializers.users import (UserModelSerializer,UserSignUpSerializer,UserLoginSerializer,AccountVerificationSerializer)
from users.serializers.profiles import ProfileModelSerializer

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """ User view set """
    queryset = User.objects.filter(is_active=True, is_client=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    #def get_permissions(self):

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


    @action(detail=True,methods=['get','put','patch'])
    def profile(self,request,*args,**kwargs):
        """"update profile data"""
        profile=Profile.objects.get() 
        queryset = self.get_queryset()
        a= queryset.values()    
        print(a)
        user = get_object_or_404(queryset)        

        partial = request.method=='PATCH'
        serializer = ProfileModelSerializer(
            profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)