from django.db import models

# Create your models here.
class Registration(models.Model):
     
    name =models.CharField(max_length=100)
    govt_id = models.CharField(max_length=100)
    email_id= models.EmailField(max_length=254)
    password = models.CharField(max_length=20) 