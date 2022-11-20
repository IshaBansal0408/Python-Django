from django.shortcuts import render
from django.views.generic import(
    ListView,
    DetailView
)
from main import models
# Create your views here.
class Index(ListView):
    template_name = 'main/index.html'
    model = models.Question
    context_object_name = 'question_list'
    
class Question(DetailView):
    model = models.Question
    template_name ='main/question.html'