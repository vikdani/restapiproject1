from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)
    mobile_num = models.IntegerField(max_length=15)

    