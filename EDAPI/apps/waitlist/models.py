from django.db import models
from apps.acads.models import Timestamps
# Create your models here.
class Waitlist(Timestamps,models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
	notes = models.TextField()
	level = models.IntegerField()

	def full_name(self):
		return f'{self.first_name} {self.last_name}'