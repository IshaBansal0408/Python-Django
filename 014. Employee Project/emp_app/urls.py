from django.urls import path
from emp_app import views
urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employees, name='employees')
]
