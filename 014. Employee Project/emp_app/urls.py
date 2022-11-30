from django.urls import path
from emp_app import views
urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employees.as_view(), name='employees'),
    path('addEmployee/', views.addEmployee.as_view(), name='addEmployee'),
    path('filterEmployee/', views.filterEmployee, name='filterEmployee'),
    path('removeEmployee/<int:pk>',
         views.removeEmployee.as_view(), name="removeEmployee"),
    path('viewEmployee/<int:pk>',
         views.viewEmployee.as_view(), name="viewEmployee"),
    path('updateEmployee/<int:pk>',
         views.updateEmployee.as_view(), name="updateEmployee"),

]
