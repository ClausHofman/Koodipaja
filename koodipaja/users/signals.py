from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

# imports for email
from django.core.mail import send_mail
import os


# @receiver(post_save, sender=Profile) # signal with decorator
def createProfile(sender, instance, created, **kwargs):
    # new user created -> create a profile for that user
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )

# comment this out if not using this, or errors at signup
        send_mail(
            "Welcome!",
            "This is a development test email message.",
            os.getenv("app_email"),
            [profile.email],
            fail_silently=False,
        )


def updateUser(sender, instance, created, **kwargs):
    # take advantage of OnetoOne-relationship
    # profile = instance.user

    if created == False:  # important
        profile = instance
        user = profile.user
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


# auto delete a user on profile deletion
def deleteUser(sender, instance, **kwargs):
    # had to use try-except, or the delete wouldn't work
    try:
        user = instance.user
        user.delete()
    except:
        pass


# auto create profile on user creation
post_save.connect(createProfile, sender=User)

# if profile is updated, trigger updateUser
post_save.connect(updateUser, sender=Profile)

# auto delete a user on profile deletion
post_delete.connect(deleteUser, sender=Profile)


# def profileUpdated(sender, instance, created, **kwargs):
#     print('Profile Saved!')
#     print('Instance:', instance)
#     print('CREATED:', created)
