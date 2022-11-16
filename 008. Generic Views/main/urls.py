from django.urls import path
from main import views
urlpatterns = [
    path('',views.Index.as_view(),name="index"),
    path('college/<int:pk>',views.CollegeDetail.as_view(),name="getCollege"),
    path('college/',views.CollegeList.as_view(),name="allCollege"),
    path('createCollege', views.CollegeCreate.as_view(),name="create_college"),
    path('student/<int:pk>',views.StudentDetail.as_view(),name="getstudent"),
    path('student/',views.StudentList.as_view(),name="allstudent"),
    path('createStudent', views.StudentCreate.as_view(),name="create_student"),
    path('updateCollege/<int:pk>',views.UpdateCollege.as_view(),name='updateCollege'),
    path('deleteCollege/<int:pk>',views.DeleteCollege.as_view(),name="deleteCollege"),
    path('updateStudent/<int:pk>',views.UpdateStudent.as_view(),name='updateStudent'),
    path('deleteStudent/<int:pk>',views.DeleteStudent.as_view(),name="deleteStudent")
]