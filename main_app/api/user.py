from main_app.models import  Field, Coordinates
from django.contrib.auth.models import User

from ..serializers import UserSerializer, UserCreateSerializer , FieldSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets , permissions
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes , permission_classes
from django.core import serializers


class UserView(APIView):

    authentication_classes = [TokenAuthentication]

    def get(self, request, **kwargs):#Get authenticated user's data
        if request.user.is_authenticated:
            serialize = UserSerializer(request.user)
            
            return Response(serialize.data , status=status.HTTP_200_OK)
        else:  return Response({"detail": "You are not logged in"},status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, **kwargs): #Create new user
        serialized = UserCreateSerializer(data=request.data)
        if serialized.is_valid():
            user = User.objects.create_user(
                serialized.validated_data['username'], 
                serialized.validated_data['email'],
                serialized.validated_data['password']
            )

            token = Token.objects.create(user=user)
            return Response({"token" : token.key }, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self , request):
        pass

 
    def delete(self , request):
        pass


@api_view(["GET"])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated, ))
def fields_of_user(request):
    fields = Field.objects.filter(owner=request.user)
    serializer = FieldSerializer(fields, many=True)
    return Response(serializer.data , status=status.HTTP_200_OK)
