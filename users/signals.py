from  django.db.models.signals import post_save
from django.contrib.auth.models import User  
from django.dispatch import receiver
from .models import Profile , Follower


@receiver(post_save,sender = User)
def create_profile(sender , instance,created,**kargs):
    if created:
        Profile.objects.create(user = instance)
        Follower.objects.create(user = instance)

@receiver(post_save,sender = User)
def save_profile(sender , instance,**kargs):
    instance.profile.save()
    instance.user.save()




