from django.shortcuts import render
from emp_app import models
from emp_app import forms
from django.http import HttpResponse, HttpResponseRedirect
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
    deptList = models.Department.objects.all()
    noResult = False
    # print(deptList)
    if (request.method == "POST"):
        # print("Requested Department:", request.POST.get('department'))
        queryset = models.Employee.objects.filter(
            department__name=request.POST.get('department'))
        # print(queryset)
        if (not queryset):
            noResult = True
        context = {
            'department_Names': deptList,
            'filteredEmployees': queryset,
            'noResult': noResult
        }
        # return HttpResponse(queryset)
        return render(request, 'emp_app/filterEmployee.html', context)
    queryset = models.Employee.objects.none()
    # print(queryset)
    context = {
        'department_Names': deptList,
        'filteredEmployees': queryset
    }
    return render(request, 'emp_app/filterEmployee.html', context)
