from django import forms

from apps.bucketlistapi.models import Bucket, Bucketlist, Review


class BucketForm(forms.ModelForm):
    class Meta:
        model = Bucket
        fields = ["title", "description"]

class BucketlistForm(forms.ModelForm):
    class Meta:
        model = Bucketlist
        fields = ["name", "description", "file_upload"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["review", "rating"]