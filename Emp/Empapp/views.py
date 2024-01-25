# views.py
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import DepartmentForm, SalaryReportForm  # Add SalaryReportForm import
from .models import Employee, Department, EmployeeSalary  # Remove DateRange import
from django.db.models import Sum
from django.utils import timezone
from django.http import HttpResponseServerError

def home(request):
    return render(request, 'home.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee.html', {'employees': employees})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department.html', {'departments': departments})

def admin_page(request):
    # Add logic for admin page
    return render(request, 'admin_page.html')




def Salary_Report(request):
    # Retrieve distinct start dates
    date_ranges = EmployeeSalary.objects.values('date_range').distinct()

    form = SalaryReportForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        selected_date_range = form.cleaned_data['date_range']

        # Filter by the date range
        employee_salaries = (
            EmployeeSalary.objects
            .filter(date_range=selected_date_range)
            .values('employee__emp_name')
            .annotate(total_salary=Sum('salary'))
        )

        context = {
            'employee_salaries': employee_salaries,
            'date_ranges': date_ranges,
        }

        return render(request, 'Salary_Report.html', context)

    return render(request, 'Salary_Report.html', {'date_ranges': date_ranges, 'form': form})
