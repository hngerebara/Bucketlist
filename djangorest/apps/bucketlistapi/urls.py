from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = {
    url(r'^bucket$',
        views.BucketView.as_view(),
        name="buckets"
        ),
    url(r'^bucket/create$',
        views.BucketView.as_view(),
        name="create_bucket"
        ),
    url(r'^bucket/(?P<bucket_id>[0-9]+)',
        views.BucketDetailView.as_view(),
        name="bucket"
        ),
    url(r'^bucketlist$',
        views.BucketlistView.as_view(),
        name="bucketlists"
        ),
    url(r'^bucketlist/(?P<bucketlist_id>[0-9]+)$',
        views.BucketlistDetailView.as_view(),
        name="bucketlist"
        ),
    url(r'^bucketlist/(?P<bucketlist_id>[0-9]+)/reviews$',
        views.ReviewListView.as_view()
        ),
    url(r'^bucketlist/(?P<bucketlist_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)$',
        views.ReviewDetailView.as_view()
        ),
}

urlpatterns = format_suffix_patterns(urlpatterns)
