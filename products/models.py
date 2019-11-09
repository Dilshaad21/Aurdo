from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Audio_Bill(models.Model):
    audio_file=models.FileField(upload_to='audio/')
