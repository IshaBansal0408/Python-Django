from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
    LogoutView as Logout
)
# Create your views here.


class Login(LoginView):
    pass
