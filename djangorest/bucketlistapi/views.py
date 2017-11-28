# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import BucketlistSerializer, ReviewSerializer
from .models import Bucketlist, Review


class BucketlistView(APIView):

    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        bucketlists = Bucketlist.objects.all()
        serializer = BucketlistSerializer(bucketlists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BucketlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BucketlistDetailView(APIView):

    permission_classes = (IsAdminOrReadOnly,)

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

class ReviewListView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

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
