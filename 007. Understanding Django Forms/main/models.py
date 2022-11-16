from django.db import models

# Create your models here.
class Student(models.Model):
    GENDERS = (
        ('f','Female'),
        ('m', 'Male')
    )
    name = models.CharField(max_length=256)
    rollNo = models.IntegerField()
    gender = models.CharField(max_length=1,choices=GENDERS)
    
    def __str__(self):
        return self.name