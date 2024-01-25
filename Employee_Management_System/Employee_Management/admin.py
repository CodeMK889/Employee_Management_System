from django.contrib import admin
from .models import Employee
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Address','Gender','Department','designation','Start_date','End_date','Salary','Promotion')




