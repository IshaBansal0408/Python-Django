from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from api import serializers
# Create your views here.

class Student :
    def __init__(self,n,r,m):
        self.name = n
        self.rollNo = r
        self.marks = m


# converts request object type from HTML to JSON
@api_view()
def usersApi(request):
    student1 = Student('A',1,23)
    student2 = Student('B',2,34)
    student3 = Student('C',3,45)
    student4 = Student('D',4,12)
    response = serializers.StudentSerial([
        student1,student2,student3
    ],many=True)
    # return HttpResponse(users)
    # return HttpResponse(json.dumps(users))
    # return Response(student)
    return Response(response.data)