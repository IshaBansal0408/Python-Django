from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here
def index(request):
    context = {}
    return render(request, 'emp_app/index.html', context)


def employees(request):
    context = {}
    return render(request, 'emp_app/employees.html', context)


def addEmployee(request):
    context = {}
    return render(request, 'emp_app/addEmployee.html', context)


def filterEmployee(request):
    context = {}
    return render(request, 'emp_app/filterEmployee.html', context)
