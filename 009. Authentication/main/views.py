from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/auth/login')
def index(request):
    context ={}
    return HttpResponse("This is the Index Page")
    # return render(request,'main/index.html',context)