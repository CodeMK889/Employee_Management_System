from django.shortcuts import render
from Emp_Salary_Management.models import Salary
# Create your views here.

def Salary_Report(request):
    salary_reports = Salary.objects.all()
    return request(request, 'Salary_Report.html', {'Salary': salary_reports})


