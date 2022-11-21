from django.shortcuts import render
from social import models

from django.views.generic import(
    ListView
)

from django.contrib.auth.mixins import(
    LoginRequiredMixin
)

# Create your views here.

# will display post of all friends
class Wall(LoginRequiredMixin, ListView):
    allPosts = models.Post.objects.all()
    model = models.Post
    context_object_name = 'allPosts'
    template_name = 'social/wall.html'
    