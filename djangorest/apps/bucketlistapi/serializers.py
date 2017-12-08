from rest_framework import serializers
from .models import Bucket, Bucketlist, Review


class ReviewSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('date_added',)

    def validate_rating(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError(
            'The rating value must be between 1 and 5'
        )

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializers to map the model int JSON format."""
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Bucketlist
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')

class BucketSerializer(serializers.ModelSerializer):
    """Serializers to map the model int JSON format."""
    bucketlists = BucketlistSerializer(many=True, read_only=True)

    class Meta:
        model = Bucket
        fields = '__all__'
        read_only_fields = ('date_created',)