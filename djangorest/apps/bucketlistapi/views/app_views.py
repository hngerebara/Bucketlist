# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from apps.bucketlistapi.models import Bucket, Bucketlist, Review
from apps.bucketlistapi.forms import app_forms, authentication_form

def CreateBucket(request):
    form = app_forms.BucketForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Successfully Created.')
        return redirect('bucketlist-app:buckets')
    else:
        messages.error(request, 'Not Successfully Created.')
    context = {
        'form': form
    }
    return render(request, 'create_bucket_form.html', context)

def ListBuckets(request):
    queryset_list = Bucket.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset_list, 6)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'buckets': queryset,
        'title': 'Buckets'
    }
    return render(request, 'dashboard.html', context)

def BucketDetail(request, bucket_id):
    instance = get_object_or_404(Bucket, pk=bucket_id)
    return render(request, 'bucketlists.html', {'bucket': instance})

def UpdateBucket(request, bucket_id=None):
    instance = get_object_or_404(Bucket, pk=bucket_id)
    form = app_forms.BucketForm(request.POST or None, instance=instance)
    if form.is_valid():
        bucket_instance = form.save(commit = False)
        bucket_instance.save()
        messages.success(request, 'Successfully Created.')
        return redirect('bucketlist-app:bucket', bucket_id=instance.id)

    context = {
        'title': instance.title,
        'form': form,
        'bucket': instance
    }
    return render(request, 'create_bucket_form.html', context)

def DeleteBucket(request, bucket_id=None):
    instance = get_object_or_404(Bucket, pk=bucket_id)
    instance.delete()
    messages.success(request, 'Successfully Deleted.')
    return redirect('bucketlist-app:buckets')

def CreateBucketlist(request, bucket_id):
    form = app_forms.BucketlistForm(request.POST or None, request.FILES or None)
    bucket = Bucket.objects.get(pk=bucket_id)

    if form.is_valid():
        bucketlist = form.save(commit=False)
        bucketlist.bucket= bucket
        bucketlist.save()
        messages.success(request, 'List Successfully Created.')
        return redirect('bucketlist-app:buckets')
    else:
        messages.error(request, 'List Not Successfully Created.')
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)

def UpdateBucketlist(request, bucket_id, bucketlist_id):
    instance = get_object_or_404(Bucketlist, pk=bucketlist_id)
    form = app_forms.BucketlistForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        bucketlist = form.save(commit=False)
        bucketlist.save()
        messages.success(request, 'List Successfully Updated.')
        return redirect('bucketlist-app:buckets')
    else:
        messages.error(request, 'List Not Successfully Updated.')
    context = {
        'form': form,
        'bucketlist': instance
    }
    return render(request, 'form.html', context)

def DeleteBucketlist(request, bucket_id, bucketlist_id):
    instance = get_object_or_404(Bucketlist, pk=bucketlist_id)
    instance.delete()
    return redirect('bucketlist-app:buckets')

def CreateBucketlistReview(request, bucket_id, bucketlist_id):
    bucketlist = Bucketlist.objects.get(pk=bucketlist_id)
    form = app_forms.ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.bucketlist= bucketlist
        review.save()
        messages.success(request, 'Review Successfully Created.')
        return redirect('bucketlist-app:buckets')
    else:
        messages.error(request, 'List Not Successfully Created.')
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)

def UpdateBucketlistReview(request, bucket_id, bucketlist_id, review_id):
    instance = get_object_or_404(Review, pk=review_id)
    form = app_forms.ReviewForm(request.POST or None, instance=instance)

    if form.is_valid():
        review = form.save(commit=False)
        review.save()
        messages.success(request, 'Review Successfully Created.')
        return redirect('bucketlist-app:buckets')
    else:
        messages.error(request, 'List Not Successfully Created.')
    context = {
        'form': form,
        'review': instance
    }
    return render(request, 'form.html', context)

def DeleteBucketlistReview(request, bucket_id, bucketlist_id, review_id):
    instance = Review.objects.get(pk=review_id)
    instance.delete()
    return redirect('bucketlist-app:buckets')

