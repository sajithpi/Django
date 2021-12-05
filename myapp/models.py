from typing import Text
from django.db import models
from django.db.models.fields import EmailField, IntegerField, TextField
from sorl.thumbnail import ImageField


# Create your models here.

class UserDetail(models.Model):
    name =  models.CharField(max_length=155,null=False,blank=False)
    age = IntegerField(blank=False,null=False)
    email = EmailField(max_length=155,blank=False,null=False)
    place = models.CharField(max_length=155,null=False,blank=False)
    occupation = models.CharField(max_length=155,null=False,blank=False)
    gender = models.CharField(max_length=155,null=False,blank=False)
    image = ImageField()


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('detail')


