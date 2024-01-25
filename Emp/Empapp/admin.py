# admin.py
from django.contrib import admin
from .models import Department, Employee, EmployeeSalary

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_name', 'email', 'designation', 'reporting_manager', 'department')


class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ['employee', 'salary', 'date_range', 'description', 'salary_by_month']

admin.site.register(EmployeeSalary, EmployeeSalaryAdmin)