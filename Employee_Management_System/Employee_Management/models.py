from django.db import models

# Create your models here.

Destination_Choices = (('Associate','Associate'), ('TL','TL'), ('Manager','Manager'))
                        

class Employee(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Address = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    Department = models.CharField(max_length=10)
    designation = models.CharField(max_length=50, choices=Destination_Choices)
    Start_date = models.DateTimeField(auto_now_add=True)
    End_date = models.DateTimeField(auto_now_add=True)
    Salary = models.IntegerField()
    Promotion = models.IntegerField()

