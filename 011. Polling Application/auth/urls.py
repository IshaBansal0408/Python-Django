from django.urls import path
from auth import views
urlpatterns = [
    path('login/',views.LoginUser.as_view(),name='login'),
    path('logout/', views.LogoutUser.as_view(),name='logout')
]