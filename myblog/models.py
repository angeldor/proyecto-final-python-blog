from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Mi Fantastico Blog')
    subtitle = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now(), null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home') 