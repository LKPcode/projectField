from django.db import models
from django.contrib.auth.models import User



class Field(models.Model):
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to ='uploads/')
    surface_area = models.DecimalField(max_digits=10, decimal_places=3 , default=0)
    num_of_trees = models.IntegerField( default=None)

    def __str__(self):
        return self.location

class Coordinates(models.Model):
    field = models.ForeignKey(Field , on_delete=models.CASCADE , default=None)
    x_value = models.DecimalField(max_digits=21, decimal_places=10)
    y_value = models.DecimalField(max_digits=20, decimal_places=10) 

    