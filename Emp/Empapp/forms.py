# forms.py
from django import forms
from .models import Department, Employee, EmployeeSalary

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'floor']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_name', 'email', 'address', 'designation', 'reporting_manager', 'department']

class EmployeeSalaryForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = ['employee', 'salary', 'date_range', 'description', 'salary_by_month']

    def clean(self):
        cleaned_data = super().clean()
        date_range = cleaned_data.get('date_range')

        if date_range == 'start_date':
            start_date = cleaned_data.get('start_date')
            end_date = cleaned_data.get('end_date')

            if start_date and end_date and start_date > end_date:
                raise forms.ValidationError('End date must be after or equal to the start date.')

        return cleaned_data


class SalaryReportForm(forms.Form):
    # Your form fields go here
    date_range = forms.CharField()  # Adjust this based on your form fields

    def clean(self):
        cleaned_data = super().clean()
        date_range = cleaned_data.get('date_range')

        # Add your custom validation for date_range if needed

        return cleaned_data





