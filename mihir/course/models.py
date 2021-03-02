from django.db import models

# Create your models here.
class Course(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20)
    Password=models.CharField(max_length=20)