from turtle import title
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Covid(models.Model):
    title = models.CharField(max_length=500)
    troubled = models.CharField(max_length=5)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    level = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title   

class Post(models.Model):
    title = models,models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    def __str__(self):
        return f"self.title"