from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pay(models.Model):
    pi_id = models.CharField(max_length = 100)
    #buyer = models.OneToOneField(User,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    ssid = models.CharField(max_length = 100)
    #added after stripe start
    def __str__(self):
        return self.user.username
    #added after stripe end
