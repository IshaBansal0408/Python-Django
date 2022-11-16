from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from main import models

from django.views.generic import(
    DetailView, 
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.

class Index(View):
    def get(self,request):
        return HttpResponse("GET Request")
    
    def post(self,request):
        return HttpResponse("POST Request")

# Detail View
# List View
# Create View
# Update View
# Delete View
  
class CollegeDetail(DetailView):
    # Meta data
    model = models.College
    template_name = 'main/college_detail.html'

class CollegeList(ListView):
    model = models.College
    template_name = 'main/college_list.html'
    context_object_name = 'allColleges'

class CollegeCreate(CreateView):
    model = models.College
    template_name = 'main/cCollege.html'
    fields = '__all__'
    success_url = '/college'

class StudentDetail(DetailView):
    # Meta data
    model = models.Student
    template_name = 'main/student_detail.html'

class StudentList(ListView):
    model = models.Student
    template_name = 'main/student_list.html'
    context_object_name = 'allStudents'

class StudentCreate(CreateView):
    model = models.Student
    template_name = 'main/cstudent.html'
    fields = '__all__'
    success_url = '/student'

class UpdateCollege(UpdateView):
    model = models.College
    template_name = 'main/cCollege.html'
    fields = '__all__'
    success_url = '/college'
    
class DeleteCollege(DeleteView):
    model = models.College
    template_name = 'main/confirm.html'
    success_url = '/college'
    

class UpdateStudent(UpdateView):
    model = models.Student
    template_name = 'main/cstudent.html'
    fields = '__all__'
    success_url = '/student'
    
class DeleteStudent(DeleteView):
    model = models.Student
    template_name = 'main/confirm.html'
    success_url = '/student'