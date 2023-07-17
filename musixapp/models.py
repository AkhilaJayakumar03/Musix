from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class songupload(models.Model):
    filmname=models.CharField(max_length=250)
    musicname=models.CharField(max_length=250)
    image=models.FileField(upload_to='musixapp/static')
    singers=models.CharField(max_length=250)
    language=models.CharField(max_length=250)
    audio=models.FileField(upload_to='musixapp/static')

    def __str__(self):
        return (self.musicname)


class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class like(models.Model):
    filmname = models.CharField(max_length=250)
    musicname = models.CharField(max_length=250)
    image = models.FileField()
    singers = models.CharField(max_length=250)
    audio = models.FileField()
    userid = models.IntegerField()

    def __str__(self):
        return (self.musicname)

