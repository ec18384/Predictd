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
    probability = models.DecimalField(decimal_places=2, max_digits=4, default=00.00)
    profile_picture_url = models.TextField(default="/static/assets/img/team-2.jpg")
