from django.urls import path 
from . import views
urlpatterns = [
    path('employee', views.Employee, name = 'employee_list' ),
]




