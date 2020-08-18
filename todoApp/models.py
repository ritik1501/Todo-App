from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title

class Vichar(models.Model):
    vichar = models.TextField(max_length=3000)

    def __str__(self):
        return self.vichar[:20]+'...'
    
    

