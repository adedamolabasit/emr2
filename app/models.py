from pydoc import describe
from turtle import title
from django.db import models

# Create your models here.

class Test(models.Model):
    name=models.CharField(max_length=211)
    doubt = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return self.name