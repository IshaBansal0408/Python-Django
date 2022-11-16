from django.shortcuts import render
from main import (
    forms,
    models
)
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    context={
        'form':forms.ExampleForm
    }
    return render(request,'main/index.html',context)

def addStudent(request):
    studentForm = forms.StudentForm()
    if(request.method == 'POST'):
          studentForm = forms.StudentForm(request.POST)
          if(studentForm.is_valid()):
              savedStudent = studentForm.save()
              return HttpResponseRedirect('/allstudents')
    context={
        'stuF' : studentForm
    }
    return render(request,'main/addStudent.html',context)

def allStudents(request):
    allStu = models.Student.objects.all()
          
    context={
        'allStudents' : allStu
    }
    return render(request,'main/students.html',context)