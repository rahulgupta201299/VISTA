from django.db import models
from apps.acads.models import Timestamps
# Create your models here.
class Competitions(Timestamps,models.Model):
	name = models.CharField(max_length=100)
	year = models.CharField(max_length=100,default='2020')