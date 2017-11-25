# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from djangorest.bucketlistapi.serializers import BucketSerializer, BucketlistSerializer
from djangorest.bucketlistapi.models import Bucket, Bucketlist


# Create your views here.

class BucketCreateView(APIView):
    """
       Create a Bucket
    """

    def post(self, request, format=None):
        serializer = BucketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BucketRetrieveView(APIView):
    """
       List all Buckets
    """
    def get(self, request, format=None):
        buckets= Bucket.objects.all()
        serializer = BucketSerializer(buckets, many=True)
        return Response(serializer.data)


class BucketUpdateView(APIView):
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

class BucketDeleteView(APIView):
    """
       Delete a Bucket
    """
    def delete(self, request, pk, format=None):
        bucket = self.get_object(pk)
        bucket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BucketlistCreateView(APIView):
    """
        Create a bucketlist
    """
    def post(self, request, format=None):
        serializer = BucketlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BucketlistRetriveView(APIView):
    """
        Retrieves all bucketlist
    """
    def get(self, request, format=None):
        bucketlist = self.Bucketlist.objects.all()
        serializer = BucketlistSerializer(bucketlist)
        return Response(serializer.data)

class BucketlistSingleRetriveView(APIView):
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

class BucketlistUpdateView(APIView):
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

class BucketlistDeleteView(APIView):
    """
        Delete a bucketlist
    """
    def delete(self, request, pk, format=None):
        bucketlist = self.get_object(pk)
        bucketlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
