from django.db import models

# Create your models here.
class contact2 (models.Model):
    
    name = models.CharField(max_length=100)
    email =models.CharField(max_length=100)
    contact_no = models.TextField()
    message = models.TextField()
   
   