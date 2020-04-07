from rest_framework import serializers
from main_app.models import  Field , Coordinates
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email" , "password"]


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = [ "id" , "location", "description", "image", "surface_area", "num_of_trees" ]


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = '__all__'