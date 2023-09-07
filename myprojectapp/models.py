import os
from uuid import uuid4
from django.db import models
from django.utils.text import slugify

class Task(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='image/', default='image/test.png')
    
    def __str__(self):
        return self.title
    
class Tool(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='image/', default='image/test.png')
    
    def __str__(self):
        return self.title
