# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from apps.bucketlistapi.models import Bucket, Bucketlist, Review
from apps.bucketlistapi.forms import BucketForm

def CreateBucket(self, request):
    form = BucketForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        'form': form
    }
    return render(request, 'create_bucket_form.html', context)

def ListBuckets(request):
    all_buckets = Bucket.objects.all()
    context = {
        'buckets': all_buckets,
        'title': 'Buckets'
    }
    return render(request, 'dashboard.html', context)

def BucketDetail(request, bucket_id):
    bucket = get_object_or_404(Bucket, pk=bucket_id)
    return render(request, 'bucketlists.html', {'bucket': bucket})

def UpdateBucket(request, bucket_id):
    bucket = get_object_or_404(Bucket, bucket_id=bucket_id)
    if request.method == "POST":
        form = BucketForm(request.POST, instance=bucket)
        if form.is_valid():
            bucket = form.save(commit = False)
            bucket.save()
            return redirect('buckets', bucket_id=bucket.bucket_id)
    else:
        form = BucketForm(instance=bucket)
    return render(request, 'create_bucket_form.html', {'form': form})



