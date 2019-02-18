from django.db import models
from main.models import *

class cabprosessing(models.Model):
    requestid=models.PositiveIntegerField()
    servicetype=models.CharField(max_length=250)
    source=models.CharField(max_length=250)
    destnation=models.CharField(max_length=250)
    Date=models.DateField()
    Pickuptime=models.TimeField()
    issuedto=models.CharField(max_length=250)
    Empid=models.ForeignKey(Consumer_Db,on_delete=models.CASCADE)
    Drivername=models.CharField(max_length=250)
    status=models.CharField(max_length=250)
    fare=models.PositiveIntegerField()
    location=models.CharField(max_length=250)
