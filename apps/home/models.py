# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class MBTITest(models.Model):
    initiator = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.TextField()
    input = models.TextField()
    date = models.DateTimeField()
    type = models.TextField(max_length=4)
    IvsE = models.TextField(max_length=1, default="")
    IvsS = models.TextField(max_length=1, default="")
    TvsF = models.TextField(max_length=1, default="")
    JvsP = models.TextField(max_length=1, default="")
    probability = models.DecimalField(decimal_places=2, max_digits=4, default=00.00)
    profile_picture_url = models.TextField(default="/static/assets/img/profileHolder.png")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.TextField(default="Software Engineer")
    team = models.TextField(default="App Development")
    testResult = models.ForeignKey(MBTITest, on_delete=models.CASCADE, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class mbtiModel(models.Model):
    typeName = models.TextField(default="")
    typeNickname = models.TextField(default="")
    workStyleSummary = models.TextField(default="")
    communication = models.TextField(default="")
    meeting = models.TextField(default="")
    emailing = models.TextField(default="")
    feedback = models.TextField(default="")
    conflict = models.TextField(default="")
    conclusion = models.TextField(default="")
    headerImgUrl = models.TextField(default="")
    overview = models.TextField(default="")
    strengths = models.TextField(default="")
    weaknesses = models.TextField(default="")
