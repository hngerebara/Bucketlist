from rest_framework import serializers
from .models import Bucket, Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializers to map the model int JSON format."""

    class Meta:
        """ Meta class to map serializers fields with the model fields."""
        model = Bucketlist
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')

class BucketSerializer(serializers.ModelSerializer):
    """Serializers to map the model int JSON format."""
    bucketlists = BucketlistSerializer(read_only=True, many=True)
    class Meta:
        """ Meta class to map serializers fields with the model fields."""
        model = Bucket
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')
