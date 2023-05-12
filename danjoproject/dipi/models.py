from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=25,blank=False,null=False)
    lname=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField()
    password=models.CharField(max_length=6)

    def __str__(self):
        return self.name

