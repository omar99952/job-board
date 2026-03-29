from django.db import models
from  django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE)
    city =  models.ForeignKey("City", on_delete=models.CASCADE) 
    image = models.ImageField( upload_to='profile/', )
    phone = models.CharField(max_length= 15)

# Signal  create new use --> create new profile
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    


class City(models.Model):
    name = models.CharField( max_length=50)