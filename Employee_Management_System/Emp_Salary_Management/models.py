from django.db import models
from Employee_Management.models import Employee
# Create your models here.


class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()




