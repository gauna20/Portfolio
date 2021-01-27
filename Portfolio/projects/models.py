from django.db import models

# Create your models here.
class Project(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=5000)
    role = models.CharField(max_length=100)
    
