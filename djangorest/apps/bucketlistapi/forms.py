from django import forms

from .models import Bucket

class BucketForm(forms.ModelForm):
    class Meta:
        model = Bucket
        fields = ["title", "description"]