from django.db import models

# Create your models here.

class My_work(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    caption = models.TextField()