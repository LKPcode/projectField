from rest_framework import routers
from main_app.api.user import UserViewSet , create_user

from main_app.api.field import FieldView 
from main_app.api.coordinates import  CoordinatesView

from django.urls import path 
from rest_framework.authtoken import views

router = routers.DefaultRouter()

#Add ViewSets Here
router.register('users', UserViewSet , "users")
#router.register('fields', FieldViewSet , "fields")
#router.register('xy', CoordinatesViewSet , "xy")

#add APIViews Here
urlpatterns = [
    #path('auth/', ExampleView.as_view()),
    path('create_user/', create_user ),
    path('api-token-auth/', views.obtain_auth_token),
    path('fields/', FieldView.as_view()),
    path('fields/<int:id>', FieldView.as_view()),
    path('xy/', CoordinatesView.as_view()),
    path('xy/<int:id>', CoordinatesView.as_view())
]

urlpatterns += router.urls
