from django.urls import path
from main import views

urlpatterns = [
    path('',views.index,name="index"),
    path('addStudent',views.addStudent,name="addStudent"),
    path('allstudents',views.allStudents,name="allStudents")
]