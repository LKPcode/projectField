from rest_framework import routers
from .api import UserViewSet, FieldViewSet , CoordinatesViewSet , create_user, get_fields, get_coordinates_of_field ,create_field
from django.urls import path 
from rest_framework.authtoken import views

router = routers.DefaultRouter()

#Add ViewSets Here
router.register('users', UserViewSet , "users")
router.register('fields', FieldViewSet , "fields")
router.register('xy', CoordinatesViewSet , "xy")

#add APIViews Here
urlpatterns = [
    #path('auth/', ExampleView.as_view()),
    path('create_user/', create_user ),
    path('get_fields/', get_fields ),
    path('create_field/', create_field ),
    path('get_coordinates_of_field', get_coordinates_of_field),
    path('api-token-auth/', views.obtain_auth_token)
]

urlpatterns += router.urls
