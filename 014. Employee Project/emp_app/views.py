from django.shortcuts import render
from emp_app import models
from emp_app import forms
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DeleteView,
    UpdateView,
)
# Create your views here


def index(request):
    context = {}
    return render(request, 'emp_app/index.html', context)


class removeEmployee(DeleteView):
    model = models.Employee
    # template_name = 'main/confirm.html'
    success_url = '/employees'


class addEmployee(CreateView):
    model = models.Employee
    template_name = 'emp_app/addEmployee.html'
    fields = '__all__'
    success_url = '/employees'


class employees(ListView):
    model = models.Employee
    template_name = 'emp_app/employees.html'
    context_object_name = 'allEmployees'


class viewEmployee(DeleteView):
    model = models.Employee
    template_name = 'emp_app/viewEmployee.html'


class updateEmployee(UpdateView):
    model = models.Employee
    template_name = 'emp_app/addEmployee.html'
    fields = '__all__'
    success_url = '/employees'


def filterEmployee(request):
    context = {}
    return render(request, 'emp_app/filterEmployee.html', context)

# def employees(request):
#     allEmployess = models.Employee.objects.all()
#     # print(allEmployess)
#     context = {
#         'allEmployees': allEmployess
#     }
#     print(context)
#     return render(request, 'emp_app/employees.html', context)

# def addEmployee(request):
#     addForm = forms.AddEmployee()
#     if (request.method == "POST"):
#         addForm = forms.AddEmployee(request.POST)
#         # print(request.POST)
#         # print("post")
#         if (addForm.is_valid()):
#             addForm.save()
#             return HttpResponseRedirect('/employees')
#     context = {
#         'addForm': addForm
#     }
#     return render(request, 'emp_app/addEmployee.html', context)
