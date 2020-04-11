
from main_app.models import  Field, Coordinates
from django.contrib.auth.models import User

from ..serializers import UserSerializer, FieldSerializer, CoordinatesSerializer , CoordinatesCreateSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view


class CoordinatesView(APIView):

    authentication_classes = [TokenAuthentication]
  
    def get(self, request, **kwargs):
        id = kwargs.get('id')
        if id != None: #/api/fields/id
            field = Field.objects.filter(pk=id).first()
            coordinates = Coordinates.objects.filter(field=field)
            serializer = CoordinatesSerializer(coordinates, many=True)
            return Response(serializer.data)
        else: return Response({"detail": "Did not provide an ID of field"})
        return Response("ok")

    def post(self, request , **kwargs ):  #/api/fields/id
        if request.user.is_authenticated==True:
            id = kwargs.get('id')
            if id is not None:
                print(request.data)
                check_ownership = Field.objects.filter(owner=request.user, id=id )
                print(check_ownership)
                if len(check_ownership) == 0: return Response({"detail":"User is not the owner of the field"})
                serialized = CoordinatesCreateSerializer(data=request.data)
                field = Field.objects.filter(pk=id).first()
                print(field , serialized.is_valid())
                if serialized.is_valid():
                    data = serialized.validated_data
                    new_coordinates  = Coordinates.objects.create(field=field , x_value="0" , y_value="0" ,
                                                     world_x=data["world_x"] , world_y=data["world_y"] )
                    new_coordinates.save()
                    return Response({"detail": "Field Created with id succesfully", "id":new_coordinates.id }, status=status.HTTP_201_CREATED)
                else: return Response({"detail": "There was an error creating the Coordinates of field"},status=status.HTTP_400_BAD_REQUEST)
            else: return Response({"detail": "id of field was not provided"})
        else: return Response({"detail":"Not authorized to create coordinates for field"}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, format=None):      
        return Response({"ok": "delete"})

    def put(self, request, format=None):      
        return Response({"ok": "put"})


