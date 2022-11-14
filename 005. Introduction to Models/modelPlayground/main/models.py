from django.db import models
from django.core.validators import (
    EmailValidator,
    MinValueValidator,
    MaxValueValidator,
    validate_slug
)
from main.validators import(
    validateAgeEven
)
# Create your models here.
# Every model is a class => table created
#every row of database is rep by an object of class
class Student(models.Model):
    GENDERS = (
        ('f','Female'),
        ('m','Male'),
        ('u','Undisclosed')
    )
    
# Varchar(100)
    name = models.CharField(max_length=100)
# Integer
    rollNo = models.IntegerField(unique=True)
# Text
# Can be null in db but not in ORM
    address = models.TextField(null=True)
# Phone Number
    phoneNo =  models.CharField(max_length=10,null=True,blank=True)
# Varchar with inbuilt validator
# Only in ORM level and not database level
    email = models.CharField(max_length=200, null=True, validators=[EmailValidator(message="Email Address is not valid")])
# Gender
    gender = models.CharField(max_length=1,choices=GENDERS,null=True)
    
    age = models.IntegerField(null=True,validators=[
        MaxValueValidator(150),
        MinValueValidator(8),
        validateAgeEven
    ])
    
    slug = models.CharField(max_length=100,validators=[
        validate_slug
    ],null=True)
    
    def __str__(self):
        return self.name
    