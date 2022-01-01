from django.contrib.auth.models import User
from .models import ProjectUsers
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_project_user(sender, instance, created, **kwargs):
    if created:
        print(instance.username, '__Created', created)
        ProjectUsers.objects.create(user=instance)
