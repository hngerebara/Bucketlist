from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = {
    url(r'^bucket/$',
        views.ListCreateBucket.as_view(),
        name="bucket"),
    url(r'^bucket/(?P<bucket_id>[0-9]+)',
        views.BucketDetailView.as_view(),
        name="bucket_deatil"),
    url(r'^bucketlist/$',
        views.ListCreateBucketlistView.as_view(),
        name="bucketlist"),
    url(r'^bucketlist/(?P<bucketlist_id>[0-9]+)$',
        views.BucketlistDetailView.as_view(),
        name="bucketlist_detail"),
    url(r'^bucketlist/(?P<bucketlist_id>[0-9]+)/reviews$',
        views.ListCreateReviewView.as_view(),
        name="review"),
    url(r'^bucketlist/(?P<bucketlist_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)$',
        views.ReviewDetailView.as_view(),
        name="review_detail"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
