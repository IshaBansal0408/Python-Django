from django.urls import path
from emp_app import views
urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employees, name='employees'),
    path('addEmployee/', views.addEmployee, name='addEmployee'),
    path('filterEmployee/', views.filterEmployee, name='filterEmployee'),
    path('removeEmployee/<int:pk>', views.removeEmployee, name="removeEmployee")
]
