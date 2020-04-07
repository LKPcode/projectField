from main_app.models import  Field, Coordinates
from django.contrib.auth.models import User
from rest_framework import viewsets , permissions
from .serializers import UserSerializer, FieldSerializer, CoordinatesSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FieldSerializer


class CoordinatesViewSet(viewsets.ModelViewSet):
    queryset = Coordinates.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CoordinatesSerializer




@api_view(["POST"])
def create_user(request, format=None):
    serialized = UserSerializer(data=request.data)
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


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_field(request, format=None):
    serialized = FieldSerializer(data=request.data) 
    if serialized.is_valid():
        data = serialized.validated_data
        new_field  = Field.objects.create(owner=request.user , location=data["location"] , description=data["description"] ,
                                         image=data["image"] , surface_area=data["surface_area"] , num_of_trees=data["num_of_trees"] )
        new_field.save()
        return Response({"detail": "Field Created"})
    return Response(serialized._errors)



#GET Fiels of User
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_fields(request, format=None):
    user = request.user
    fields = Field.objects.filter(owner=user)
    serializer = FieldSerializer(fields, many=True)
    return Response(serializer.data)


#get Coordinates of Field
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_coordinates_of_field(request, format=None):
    user = request.user
    field = Field.objects.filter(pk=request.data["id"]).first()
    coordinates = Coordinates.objects.filter(field=field)
    serializer = CoordinatesSerializer(coordinates, many=True)
    return Response(serializer.data)