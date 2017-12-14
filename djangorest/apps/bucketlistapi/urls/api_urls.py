from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from apps.bucketlistapi.views import api_views

urlpatterns = {
    url(r'^api/bucket/$',
        api_views.ListCreateBucket.as_view()),
    url(r'^api/bucket/(?P<bucket_id>[0-9]+)',
        api_views.BucketDetailView.as_view()),
    url(r'^api/bucketlist/$',
        api_views.ListCreateBucketlistView.as_view()),
    url(r'^api/bucketlist/(?P<bucketlist_id>[0-9]+)$',
        api_views.BucketlistDetailView.as_view()),
    url(r'^api/bucketlist/(?P<bucketlist_id>[0-9]+)/reviews$',
        api_views.ListCreateReviewView.as_view()),
    url(r'^api/bucketlist/(?P<bucketlist_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)$',
        api_views.ReviewDetailView.as_view()),

}

urlpatterns = format_suffix_patterns(urlpatterns)
