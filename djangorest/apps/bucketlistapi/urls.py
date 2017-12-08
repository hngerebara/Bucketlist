from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import api_views, app_views

app_name = 'bucketlist'
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

    url(r'^bucket/create$',
        app_views.CreateBucket,
        name="create_bucket"),
    url(r'^bucket/$',
        app_views.ListBuckets,
        name="buckets"),
    url(r'^bucket/(?P<bucket_id>[0-9]+)$',
        app_views.BucketDetail,
        name="single_bucket"),
    url(r'^bucket/(?P<bucket_id>[0-9]+)/edit$',
        app_views.UpdateBucket,
        name="update_bucket"),

}

urlpatterns = format_suffix_patterns(urlpatterns)
