from django.db import models

# Create your models here.
class Payment(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    payment_id=models.CharField(max_length=200)
    amount=models.CharField(max_length=100)
    paid=models.BooleanField(default=False)
    courseName=models.CharField(max_length=200)
    courseID=models.CharField(max_length=100)