from django.db import models

# Create your models here.

class CarBrand(models.Model):
    name=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    prize=models.CharField(max_length=50)