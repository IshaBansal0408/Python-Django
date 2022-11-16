from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=356)
    password = forms.CharField(widget=forms.PasswordInput)