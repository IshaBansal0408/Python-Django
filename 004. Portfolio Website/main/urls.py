from django import views
from django.urls import path
from main import views

urlpatterns = [
    path('',views.index)
]