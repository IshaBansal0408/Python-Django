from django.urls import path
from main import views
urlpatterns=[
    path('',views.defPage,name='defPage'),
    path('secure/',views.index,name='secure')
]