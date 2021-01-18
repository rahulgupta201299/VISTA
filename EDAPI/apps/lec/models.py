from django.db import models
from apps.acads.models import Timestamps
# Create your models here.
class Lec(Timestamps,models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	date = models.DateField()
	notes_url = models.CharField(max_length=255)
	lec_name = models.CharField(max_length=100)
	duration = models.IntegerField()
	is_required = models.BooleanField(default=True)