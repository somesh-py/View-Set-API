from django.contrib import admin
from .models import CarBrand
# Register your models here.


@admin.register((CarBrand))
class CarBrandModelAdmin(admin.ModelAdmin):
    list_display=['id','name','color','model','prize']