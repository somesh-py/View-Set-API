from django.urls import path,include
from .views import CarBrandAPI
from rest_framework import routers


routers=routers.DefaultRouter()
routers.register(r'CarBrandAPI',CarBrandAPI,basename='CarBrandAPI')

urlpatterns = [
    path('',include(routers.urls))
]
