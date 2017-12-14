# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import Bucketlist, Review

# Create your tests here.

class BucketlistModelTestCase(TestCase):
    """ This class defines the test suite for bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.bucketlist_name ="Learn Django"
        self.bucketlist_desciption ="Learning to code in python"
        self.bucketlist = Bucketlist(name=self.bucketlist_name, description=self.bucketlist_desciption)

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)


class ReviewModelTestCase(TestCase):
    """ This class defines the test suite for bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.review_title ="Review for learn django"
        self.review_review ="Learning django has been great"
        self.review_rating = 4
        self.review_created_by = "Hopez"
        self.review_bucketlistId = 1
        self.review = Bucketlist(
            title=self.review_title,
            review=self.review_review,
            rating=self.review_rating,
            created_by=self.review_created_by,
            bucketlist=self.review_bucketlistId
        )

    def test_model_can_create_a_review(self):
        old_count = Review.objects.count()
        self.review.save()
        new_count = Review.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """ Test suite for views"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Port Harcourt'}
        self.response = self.client.post(
            reverse('Create'),
            self.bucketlist_data,
            format="json")

    def test_api_can_create_a_bucketlist(self):
        """Test that a bucket has been created"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given bucketlist."""
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        bucketlist = Bucketlist.objects.get()
        change_bucketlist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)