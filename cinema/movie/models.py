from django.db import models

# Create your models here.

class movie(models.Model):
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=20)
    year=models.IntegerField()
    image=models.ImageField(upload_to="movie/sreen",null=True,blank=True)
    def __str__(self):
        return self.name