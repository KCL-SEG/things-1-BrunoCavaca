from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    name = models.CharField(unique=True, max_length=30, blank=False)
    description = models.CharField(unique=False,blank=True,max_length=120)
    quantity = models.IntegerField(unique=False,validators=[MinValueValidator(0), MaxValueValidator(100)])