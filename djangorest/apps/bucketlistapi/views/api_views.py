# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.bucketlistapi.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status, generics
from apps.bucketlistapi.serializers import BucketSerializer, BucketlistSerializer, ReviewSerializer
from apps.bucketlistapi.models import Bucket, Bucketlist, Review


class ListCreateBucket(APIView):
    # permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_buckets = Bucket.objects.all()
        serializer = BucketSerializer(all_buckets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BucketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BucketDetailView(APIView):
    def get_object(self, bucket_id):
        try:
            return Bucket.objects.get(pk=bucket_id)
        except Bucket.DoesNotExist:
            raise Http404

    def get(self, request, bucket_id, format=None):
        bucket = self.get_object(bucket_id)
        serializer = BucketSerializer(bucket)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bucket = get_object_or_404(Bucket, bucket_id=pk)
        serializer = BucketSerializer(bucket, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, bucket_id, format=None):
        bucket = self.get_object(bucket_id=bucket_id)
        bucket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListCreateBucketlistView(APIView):

    # permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_bucketlists = Bucketlist.objects.all()
        serializer = BucketlistSerializer(all_bucketlists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BucketlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BucketlistDetailView(APIView):

    # permission_classes = (IsAdminOrReadOnly,)

    def get_object(self, bucketlist_id):
        try:
            return Bucketlist.objects.get(pk=bucketlist_id)
        except Bucketlist.DoesNotExist:
            raise Http404

    def get(self, request, bucketlist_id, format=None):
        bucketlist = self.get_object(bucketlist_id)
        serializer = BucketlistSerializer(bucketlist)
        return Response(serializer.data)

    def put(self, request, bucketlist_id, format=None):
        bucketlist = self.get_object(bucketlist_id=bucketlist_id)
        serializer = BucketlistSerializer(bucketlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, bucketlist_id, format=None):
        bucketlist = self.get_object(bucketlist_id=bucketlist_id)
        bucketlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListCreateReviewView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        # Automatically set the user using the one who is logged in
        serializer.save(
            created_by=self.request.user,
            bucketlist_id=self.kwargs['bucketlist_id'])

    def get_queryset(self):
        bucketlist = self.kwargs['bucketlist_id']
        return Review.objects.filter(bucketlist_id=bucketlist)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'review_id'

    def get_queryset(self):
        review = self.kwargs['review_id']
        return Review.objects.filter(id=review)
