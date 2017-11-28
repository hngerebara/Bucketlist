# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bucket(models.Model):
    """This class represents the bucket model"""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        """Return the name of the model instance"""
        return "{}".format(self.name)

class Bucketlist(models.Model):
    """This class represents the bucketlists model"""
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(blank=True)
    bucket = models.ForeignKey(Bucket, related_name="bucketlists")
    owner = models.ForeignKey('auth.User', default=1, blank= True, null=False, related_name='bucketlistuser', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the name of the model instance"""
        return "{}".format(self.name)