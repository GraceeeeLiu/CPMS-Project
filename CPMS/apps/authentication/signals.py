from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Author, Reviewer, UserCAT

# @receiver(post_save, sender=User)
# def create_author(sender, instance, created, **kwargs):
#     if created:
#         Author.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_author(sender, instance, **kwargs):
    instance.usercat.save()

