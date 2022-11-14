from django.contrib import admin
from relationPlayground import models
# Register your models here.

admin.site.register([
    models.Article,
    models.Author,
    models.Toppings,
    models.Pizza,
    models.Person,
    models.Society,
    models.Membership
])