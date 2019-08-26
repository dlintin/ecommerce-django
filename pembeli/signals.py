from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profil


@receiver(post_save, sender=User)
def create_profil(sender, instance, created, *kwargs):
    if created:
        Profil.objects.create(user=instance)
         
@receiver(post_save, sender=User)
def save_profil(sender, instance, *kwargs):
    instance.profil.save() 