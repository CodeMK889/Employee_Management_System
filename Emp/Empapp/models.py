from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date

class Department(models.Model):
    name = models.CharField(max_length=100)
    floor = models.PositiveIntegerField()
    basic_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name
    
    def get_emp_hierarchy(self, manager=None):
        hierarchy = {'manager': manager, 'employees': []}

        if manager:
            employees = Employee.objects.filter(department=self, reporting_manager=manager)
        else:
            employees = Employee.objects.filter(department=self, reporting_manager=None)

        for employee in employees:
            hierarchy['employees'].append(self.get_emp_hierarchy(employee))

        return hierarchy

class DateRange(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.start_date} - {self.end_date}"    

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    design_choices = [("Associate", "Associate"), ("Team Leader", "Team_Leader"), ("Manager", "Manager")]
    designation = models.CharField(max_length=50, choices=design_choices)
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    joining_date = models.DateTimeField()
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
    
class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salaries')
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_choices = [("start_date", "Start Date"), ("end_date", "End Date")]
    date_range = models.CharField(max_length=10, choices=date_choices)
    description = models.TextField(blank=True, null=True)
    
    # Add decimal_places attribute to the salary_by_month field
    month_choices = [
        ("January", "January"), ("February", "February"), ("March", "March"),
        ("April", "April"), ("May", "May"), ("June", "June"),
        ("July", "July"), ("August", "August"), ("September", "September"),
        ("October", "October"), ("November", "November"), ("December", "December")
    ]
    salary_by_month = models.DecimalField(max_digits=50, decimal_places=2, default=0.0)  # Set a default value here

    def __str__(self):
        return f"{self.employee.emp_name}: {self.salary} - {self.get_date_range_display()}"