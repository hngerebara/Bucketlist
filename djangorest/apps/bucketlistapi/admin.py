# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Bucket, Bucketlist, Review

# Register your models here.
class BucketAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created"]
    search_fields = ["title"]

    class Meta:
        model = Bucket
admin.site.register(Bucket, BucketAdmin)

class BucketlistAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "date_created", "date_modified", "bucket", ]
    search_fields = ["name", "description"]

    class Meta:
        model = Bucketlist
admin.site.register(Bucketlist, BucketlistAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["review" ]

    class Meta:
        model = Review
admin.site.register(Review, ReviewAdmin)

