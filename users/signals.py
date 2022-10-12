from profile import Profile
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# @reciever(post_save, sender=profile)
def createProfile(sender,instance,created,**kwargs):
    print('profile signal triggered')
    if created:
        user = instance
        profile = Profile.objects.create(  # type: ignore
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)