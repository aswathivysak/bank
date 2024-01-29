from django.db import models

# Create your models here.
class Team(models.Model):
    tmname=models.CharField(max_length=255)
    image=models.ImageField(upload_to='pics')
    about=models.TextField()
    def __str__(self):
        return self.tmname
