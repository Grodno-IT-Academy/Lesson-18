from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.models import Group


# @receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='user')
        instance.groups.add(group)
        Profile.objects.create(user=instance)

post_save.connect(created_profile, sender=User)

@receiver(post_save, sender=User)
def updated_user(sender, instance, created, **kwargs):
    if not created:
        pass
        # instance.profile.save()