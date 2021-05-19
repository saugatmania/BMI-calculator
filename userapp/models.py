from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    GENDER = (
        ("male", "MALE"),
        ("female", "FEMALE"),
        ("other", "OTHER")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    contact = models.IntegerField(default=1)
    age = models.IntegerField(default=1)
    gender = models.CharField(max_length=20, choices=GENDER)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.user

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
