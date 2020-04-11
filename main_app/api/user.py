from main_app.models import  Field, Coordinates
from django.contrib.auth.models import User

from ..serializers import UserSerializer, FieldSerializer , FieldCreateSerializer , CoordinatesSerializer , CoordinatesCreateSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets , permissions
from rest_framework.decorators import api_view


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer



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

