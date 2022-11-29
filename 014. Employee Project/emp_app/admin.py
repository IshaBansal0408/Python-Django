from django.contrib import admin
from emp_app import models

admin.site.register([
    models.Employee,
    models.Department,
    models.Role
])
