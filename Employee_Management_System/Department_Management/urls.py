from django.urls import path 
from . import views 
urlpatterns = [

    path('department/', views.Department_list, name='department_list'),
]   