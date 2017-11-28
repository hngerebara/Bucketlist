# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import BucketSerializer, BucketlistSerializer
from .models import Bucket, Bucketlist


# Create your views here.
class BucketObject(APIView):
    def get_object(self, pk):
        try:
            return Bucket.objects.get(pk=pk)
        except Bucket.DoesNotExist:
            raise Http404

class BucketCreateView(APIView):
    """
       Creates a new bucket
    """

    def post(self, request, format=None):
        serializer = BucketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BucketView(APIView):
    """
       Retrieves all Buckets
    """

    def get(self, request, format=None):
        buckets= Bucket.objects.all()
        serializer = BucketSerializer(buckets, many=True)
        return Response(serializer.data)

class BucketSingleRetriveView(BucketObject):
    """
        Retrieve a single bucket with it's list
    """
    def get_object(self, pk):
        try:
            return Bucket.objects.get(pk=pk)
        except Bucket.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bucket = self.get_object(pk)
        serializer = BucketSerializer(bucket)
        return Response(serializer.data)

class BucketUpdateView(BucketObject):
    """
       Update a Bucket
    """
    def put(self, request, pk, format=None):
        bucket = self.get_object(pk)
        serializer = BucketSerializer(bucket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BucketDeleteView(BucketObject):
    """
       Delete a Bucket
    """
    def delete(self, request, pk, format=None):
        bucket = self.get_object(pk)
        bucket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BucketlistObject(APIView):
    def get_object(self, pk):
        try:
            return Bucketlist.objects.get(pk=pk)
        except Bucket.DoesNotExist:
            raise Http404

class BucketlistCreateView(APIView):
    """
        Creates a new bucketlist
    """

    def post(self, request, format=None):
        serializer = BucketlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BucketlistSingleRetriveView(BucketlistObject):
    """
        Retrieve a single bucketlist
    """
    def get_object(self, pk):
        try:
            return Bucketlist.objects.get(pk=pk)
        except Bucket.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bucketlist = self.get_object(pk)
        serializer = BucketlistSerializer(bucketlist)
        return Response(serializer.data)

class BucketlistUpdateView(BucketlistObject):
    """
        Update a bucketlist
    """
    def put(self, request, pk, format=None):
        bucketlist = self.get_object(pk)
        serializer = BucketlistSerializer(bucketlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BucketlistDeleteView(BucketlistObject):
    """
        Delete a bucketlist
    """
    def delete(self, request, pk, format=None):
        bucketlist = self.get_object(pk)
        bucketlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
