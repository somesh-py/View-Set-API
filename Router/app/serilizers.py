from rest_framework import serializers
from .models import CarBrand


class CarBrandSerilizer(serializers.ModelSerializer):
    class Meta:
        model=CarBrand
        fields='__all__'