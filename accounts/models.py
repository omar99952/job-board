from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE)
    city =  models.ForeignKey("City", on_delete=models.CASCADE) 
    image = models.ImageField( upload_to='profile/', )
    phone = models.CharField(max_length= 15)





class City(models.Model):
    name = models.CharField( max_length=50)