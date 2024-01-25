from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('department_list/', views.department_list, name='department_list'),  # Add the name attribute here
    path('admin/', views.admin_page, name='admin_page'),
    path('Salary_Report/', views.Salary_Report, name='Salary_Report'),

    # path('add_department/', views.Department_Form, name='add_department'),
    # path('add_employee/', views.Add_Employee, name='add_employee'),
    # path('add_salary/', views.Add_Salary, name='add_salary'),
    # path('salary_list/', views.Salary_List, name='salary_list'),
    # path('edit_employee/<int:id>/', views.Edit, name='edit_employee'),
    # path('delete_employee/', views.Delete, name='delete_employee'),
]


