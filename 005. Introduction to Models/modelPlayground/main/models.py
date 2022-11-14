from django.db import models

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
    address = models.TextField(null=True)
# Phone Number
    phoneNo =  models.CharField(max_length=10,null=True,blank=True)
# Varchar with inbuilt validator
    email = models.EmailField(null=True)
# Gender
    gender = models.CharField(max_length=1,choices=GENDERS,null=True)
    
    def __str__(self):
        return self.name
    