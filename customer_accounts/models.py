from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=150, blank=True)
    address = models.TextField(max_length=500, blank=True)
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    business_number = models.CharField(max_length=255)

@receiver(post_save, sender=User)
def create_user_business_num(sender, instance, created, **kwargs):
    if created:
        Seller.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_business_num(sender, instance, **kwargs):
    instance.seller.save()