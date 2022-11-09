from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # response = HttpResponse("Hello World")
    
    owner = "Isha Bansal"
    allUsers = ["Kartik Gupta","Isha Bansal","Harshit Gaur","Gaurav Narula"]
    show_Owner = True
    context = {
        "owner" : owner,
        "allUsers" : allUsers,
        "show_Owner" :show_Owner
    }
    
    response = render(request,"HelloWorld/index.html",context)
    return response

def welcome(request):
    response = render(request,'HelloWorld/welcome.html')
    return response