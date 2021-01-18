from django.db import models 

# Create your models here. 


class React(models.Model):
        created_at = models.DateTimeField(auto_now_add=True)
        host=models.CharField(max_length=50,unique=True)
        user= models.CharField(max_length=10)
        username = models.CharField(max_length=30) 
        password = models.CharField(max_length=50)
