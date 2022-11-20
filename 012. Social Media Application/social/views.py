from django.shortcuts import render
from social import models

from django.views.generic import(
    ListView
)

# Create your views here.

# will display post of all friends
class Wall(ListView):
    allPosts = models.Post.objects.all()
    model = models.Post
    context_object_name = 'allPosts'
    template_name = 'social/wall.html'
    