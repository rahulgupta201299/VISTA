from django.db import models

# Create your models here.
class Profile(models.Model):
    email=models.CharField(max_length=200)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    Address1=models.CharField(max_length=900)
    Address2=models.CharField(max_length=900,blank=True,null=True)
    Zip=models.CharField(max_length=10)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    DOB=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    school=models.CharField(max_length=500)
    grade=models.CharField(max_length=10)
    def __str__(self):
        return self.firstname+" "+self.lastname+" ( "+self.email+" ) "