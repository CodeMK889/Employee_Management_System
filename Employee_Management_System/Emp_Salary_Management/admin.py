from django.contrib import admin
from . models import Salary
# Register your models here.


class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee','amount','start_date','end_date')


