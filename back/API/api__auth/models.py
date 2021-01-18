from django.db import models

# Create your models here.
class Database(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    firstName = models.CharField(max_length=100)
    lastName =models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone=models.CharField(max_length=11)
    state=models.CharField(max_length=50)
    pin=models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    
 
 
    