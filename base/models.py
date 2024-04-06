from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

class MyModel(models.Model):
    Item_name = models.CharField(max_length=200)
    Quant_ity = models.IntegerField()