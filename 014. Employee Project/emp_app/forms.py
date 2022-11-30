from django import forms
from emp_app import models


class AddEmployee(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = '__all__'
