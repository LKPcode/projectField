from main_app.models import  Field, Coordinates
from django.contrib.auth.models import User

from ..serializers import UserSerializer, FieldSerializer , FieldCreateSerializer , CoordinatesSerializer , CoordinatesCreateSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status



class FieldView(APIView):

    authentication_classes = [TokenAuthentication]
  
    def get(self, request, **kwargs):

        id = kwargs.get('id')
        if id==None: #/api/fields
            fields = Field.objects.all()
            serializer = FieldSerializer(fields, many=True)
            return Response(serializer.data)
        else: #/api/fields/id
            fields = Field.objects.filter(pk=id)
            serializer = FieldSerializer(fields, many=True)
            return Response(serializer.data)
        return Response("ok")

    def post(self, request ): 
        if request.user.is_authenticated==True:
            serialized = FieldCreateSerializer(data=request.data)
            print(request.data)
            if serialized.is_valid():
                data = serialized.validated_data
                new_field  = Field.objects.create(owner=request.user , location=data["location"] , description=data["description"] ,
                                                image=data["image"] , surface_area=data["surface_area"] , num_of_trees=data["num_of_trees"] )
                new_field.save()
                return Response({"detail": "Field Created with id ", "id":new_field.id}, status=status.HTTP_201_CREATED)
            else: return Response({"detail": "There was an error creating the Field"},status=status.HTTP_400_BAD_REQUEST)
        else: return Response({"detail":"Not authorized to create a field"}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, format=None):      
        return Response({"ok": "delete"})

    def put(self, request, format=None):      
        return Response({"ok": "put"})



