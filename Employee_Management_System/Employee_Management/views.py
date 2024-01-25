from django.shortcuts import render
from . models import Employee
# Create your views here.


def Employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee.html', {'Employee': employees})


# def home(request):
#     return request(request, 'home.html')
