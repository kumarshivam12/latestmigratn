from django.db import models


# Create your models here.

class Role_Per(models.Model):
    id=models.PositiveIntegerField(primary_key=True)
    role=models.CharField(max_length=250)
    perr=models.TextField()



class Consumer_Db(models.Model):
    User_type=models.CharField(max_length=250)
    password = models.CharField(max_length=20)
    Fname = models.CharField(max_length=250)
    Mname = models.CharField(max_length=250)
    Lname = models.CharField(max_length=250)
    Email=models.EmailField(max_length=250)
    Phone=models.PositiveIntegerField(max_length=10)
    Address=models.TextField()
    Mgname=models.CharField(max_length=250)
    Mg_email=models.CharField(max_length=250)
    Location=models.TextField()
    RId = models.ForeignKey(Role_Per,on_delete=models.CASCADE)
    empid=models.PositiveIntegerField(primary_key=True)




