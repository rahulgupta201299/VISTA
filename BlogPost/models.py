from django.db import models

def upload_path(instance,filename):
    return '/'.join(['covers',str(instance.title),filename])

# Create your models here.
class BlogDetail(models.Model):
    title=models.CharField(max_length=400)
    subtitle=models.CharField(max_length=300,blank=True,null=True)
    Description=models.TextField()
    footers=models.CharField(max_length=200,blank=True,null=True)
    Attachment=models.FileField(blank=True,null=True,upload_to=upload_path)
    def __str__(self):
        return self.title