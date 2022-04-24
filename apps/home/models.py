# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import datetime

from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from core import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mbti_type = models.TextField(max_length=4, default="XXXX")
    mbti_nickname = models.TextField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class MBTITest(models.Model):
    initiator = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.TextField()
    input = models.TextField()
    date = models.DateTimeField()
    type = models.TextField(max_length=4)
    probability = models.DecimalField(decimal_places=16, max_digits=18, default=00.0000000000000000)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True,
                                        default=settings.DEFAULT_PROFILE_PICTURE_LOCATION, max_length=100000)
