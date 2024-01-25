from django.shortcuts import render
from Department_Management.models import Department
# Create your views here.



def Department_list(request):
    departments = Department.objects.all()
    return render(request, 'department.html', {'department': departments})

