# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import Bucketlist

# Create your tests here.

class ModelTestCase(TestCase):
    """ This class defines the test suite for bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.bucketlist_name =" Write world class code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
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