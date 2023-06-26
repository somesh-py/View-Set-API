from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from .models import CarBrand
from .serilizers import CarBrandSerilizer
from rest_framework.response import Response
# Create your views here.


class CarBrandAPI(viewsets.ViewSet):
    
        def list(self,request):
            data=CarBrand.objects.all()
            serilizer=CarBrandSerilizer(data,many=True)
            return Response(serilizer.data)
    
        def retrieve(self,request,pk=None):
            if pk is not None:
                data=CarBrand.objects.get(id=pk)
                serilizer=CarBrandSerilizer(data)
                return Response(serilizer.data)
        
        def create(self,request):
             serilizer=CarBrandSerilizer(data=request.data)
             if serilizer.is_valid():
                  serilizer.save()
                  return Response(serilizer.data)
             else:
                  return Response({'msg':'Data Not Created'})
        
        def update(self,request,pk):
             data=CarBrand.objects.get(id=pk)
             serilizers=CarBrandSerilizer(data,data=request.data)
             if serilizers.is_valid():
                  serilizers.save()
                  return Response(serilizers.data)
             else:
                  return Response({'msg':'Data Not Updated'})
        
        def partial_update(self,request,pk):
             data=CarBrand.objects.get(id=pk)
             serilizers=CarBrandSerilizer(data,data=request.data)
             if serilizers.is_valid():
                  serilizers.save()
                  return Response(serilizers.data)
             else:
                  return Response({'msg':'Data Partially Not Updated'})
        
        def destroy(self,request,pk):
             CarBrand.objects.filter(id=pk).delete()
             return Response({'msg':'Data Deleted Sucessfully'})