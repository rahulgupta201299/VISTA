from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpeg',upload_to ="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
#added1 start
class UserAdd(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_no = models.CharField(default = '0000000000',max_length = 255)
    address = models.CharField(default = 'None',max_length = 255)
    std = models.IntegerField(default = '8')
    upload = models.FileField(default = 'Empty')
    def __str__(self):
        #return self.user.username #added stripe
        return self.user.username
#added1 end
