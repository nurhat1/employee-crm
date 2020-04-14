
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('department/<str:pk_dep>', views.department, name = 'department'),
    path('employees/', views.employees, name='employees'),

    path('create_department/', views.createDepartment, name = 'create_department'),
    path('update_department/<str:pk_dep>', views.updateDepartment, name = 'update_department'),
    path('create_position/', views.createPosition, name = 'create_position'),
    path('add_employee/', views.addEmployee, name = 'add_employee'),
    path('update_employee/<str:pk_emp>', views.updateEmployee, name = 'update_employee'),
    path('delete_employee/<str:pk_emp>', views.deleteEmployee, name = 'delete_employee'),

    path('replace_employees/<str:pk_dep>', views.replaceEmployees, name = 'replace_employees'),

    path('get-report/', views.getReport, name = 'get-report'),
]

