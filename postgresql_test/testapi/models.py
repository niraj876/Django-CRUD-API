from django.db import models


# Create your models here.
class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    salary = models.IntegerField()

