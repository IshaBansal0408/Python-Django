from django.shortcuts import render
from django.contrib.auth.views import(
    LoginView,
    LogoutView as LogoutUser
)
# Create your views here.
class LoginUser(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True