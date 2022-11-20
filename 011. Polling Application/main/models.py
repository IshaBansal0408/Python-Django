from django.db import models

# Create your models here.
class Question(models.Model):
    content = models.CharField(max_length=256)
    slug = models.SlugField()
    def __str__(self):
        return self.content
    
class Choice(models.Model):
    content = models.CharField(max_length=256)
    question = models.ForeignKey('Question',on_delete=models.CASCADE)
    def __str__(self):
        return '{}-{}'.format(self.question.content[:50],self.content)