from django.urls import path 
from . import views

urlpatterns = [

    path('salary_report/', views.Salary_Report, name='Salary_Report' ),
]




