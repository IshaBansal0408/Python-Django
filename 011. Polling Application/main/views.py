from django.shortcuts import render
from django.views.generic import(
    ListView,
    DetailView,
    FormView,
)
from django.views.generic.detail import SingleObjectMixin
from main import models
from main import forms

from django.http import HttpResponseRedirect

# Create your views here.
class Index(ListView):
    template_name = 'main/index.html'
    model = models.Question
    context_object_name = 'question_list'
    
class Question(SingleObjectMixin, FormView):
    model = models.Question
    template_name ='main/question.html'
    form_class = forms.AnswerForm
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.question = self.get_object()
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect('')
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['canAnswer'] = models.Answer.objects.count(question = self.get_obect(), user= self.request.user)
        return data