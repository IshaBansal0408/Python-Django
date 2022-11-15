from django.urls import path
from main import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blog/<int:pk>', views.blog,name="getBlog"),
    path('author/<int:pk>', views.author,name="getAuth")
]