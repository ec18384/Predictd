# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class MBTITests(models.Model):
    initiator = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.TextField()
    input = models.TextField()
    date = models.DateTimeField()
    result = models.TextField(max_length=4)
