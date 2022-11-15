from django.shortcuts import render,get_object_or_404
from main import models
from django.http import(
    Http404
)
# Create your views here.
def index(request):
    # Queries are executed lazily
    latest_blogs =models.Blog.objects.all().order_by('-createdAt')[:10]
    
    context = {
        'latest_blogs' : latest_blogs
    }
    return render(request,'main/index.html',context)

def blog(request,pk):
    # try:
    #     blog = models.Blog.objects.get(pk = pk)
    # except:
    #     raise Http404
    blog = get_object_or_404(models.Blog,pk=pk)
    context = {
        'cBlog' : blog
    }
    return render(request,'main/blog.html',context)

def author(request,pk):
    # try:
    #     blog = models.Blog.objects.get(pk = pk)
    # except:
    #     raise Http404
    auth = get_object_or_404(models.Author,pk=pk)
    context = {
        'cAuth' : auth
    }
    return render(request,'main/author.html',context)