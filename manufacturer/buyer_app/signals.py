from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Buyer

@receiver(post_save, sender=User)
def create_buyer_profile(sender, instance, created, **kwargs):
    if created:
        Buyer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_buyer_profile(sender, instance, **kwargs):
    instance.buyer_profile.save()
