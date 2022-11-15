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

def createBlog(request):
    
    authors = models.Author.objects.all()
    context={
        'authors': authors 
    }
    
    if(request.method == "POST"):
        blogData = {
            'title': request.POST['title'],
            'content' : request.POST['content']
        }
        blog = models.Blog.objects.create(**blogData)
        auth = models.Author.objects.filter(pk = request.POST['author'])
        blog.authors.set(auth)
        
        context["success"] = True
    
    
    return render(request, 'main/createBlog.html',context)