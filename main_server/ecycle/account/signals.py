from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import Picker_Locations,User

@receiver(post_save, sender=User)
def create_email_verification_token(sender, instance, created, **kwargs):
    if created:
        if instance.is_picker==True:
            Picker_Locations.objects.create(user=instance,lat=0,long=0)

      
        