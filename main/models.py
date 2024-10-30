from django.db import models

# Create your models here.


class Destination(models.Model):
    vid = models.FileField(upload_to='videos_uploaded')


class Destination2(models.Model):
    vid = models.FileField(upload_to='videos_uploaded')


class Destination3(models.Model):
    vid = models.FileField(upload_to='videos_uploaded')

    
class Destination4(models.Model):
    vid = models.FileField(upload_to='videos_uploaded')
