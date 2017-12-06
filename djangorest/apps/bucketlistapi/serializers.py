from rest_framework import serializers
from .models import Bucket, Bucketlist, Review


class ReviewSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('date_added',)

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializers to map the model int JSON format."""
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        """ Meta class to map serializers fields with the model fields."""
        model = Bucketlist
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')

class BucketSerializer(serializers.ModelSerializer):
    """Serializers to map the model int JSON format."""
    bucketlists = BucketlistSerializer(many=True, read_only=True)
    class Meta:
        """ Meta class to map serializers fields with the model fields."""
        model = Bucket
        fields = '__all__'
        read_only_fields = ('date_created',)