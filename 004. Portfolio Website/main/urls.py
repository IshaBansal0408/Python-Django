from django.urls import path
from main import views
urlpatterns = [
    path('projects',views.project,name='projects'),
    path('languages',views.languages,name = 'languages'),
    path('',views.index,name='index')
]