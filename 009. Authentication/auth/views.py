from django.shortcuts import render
from auth import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login

# Create your views here.
def Login(request):
    logForm = forms.LoginForm()
    error = None
    if(request.method == "POST"):
        logForm = forms.LoginForm(request.POST)
        if(logForm.is_valid()):
            username = logForm.cleaned_data['username']
            password = logForm.cleaned_data['password']
            user = authenticate(username = username,password = password)
            if(user):
                print(user)
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                error = "Invalid Credentials"
 
    context = {
        'form' : logForm,
        'error' :error
    }
    return render(request, 'auth/loginForm.html',context)
