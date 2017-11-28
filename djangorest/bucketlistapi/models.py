# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bucketlist(models.Model):
    """This class represents the bucketlists model"""
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the name of the model instance"""
        return "{}".format(self.name)

class Review(models.Model):
    bucketlist = models.ForeignKey(Bucketlist, related_name='reviews')
    title = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField()
    created_by = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now_add=True)