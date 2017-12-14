from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from apps.bucketlistapi.views import app_views

urlpatterns = {
    url(r'^bucket/create$', app_views.CreateBucket, name="create_bucket"),
    url(r'^bucket/(?P<bucket_id>[0-9]+)/edit$', app_views.UpdateBucket, name="edit_bucket"),
    url(r'^bucket/(?P<bucket_id>[0-9]+)/delete$', app_views.DeleteBucket, name="delete_bucket"),
    url(r'^bucket$', app_views.ListBuckets, name="buckets"),
    url(r'^bucket/(?P<bucket_id>[0-9]+)$', app_views.BucketDetail, name="bucket"),
    url(r'^bucket/(?P<bucket_id>[0-9]+)/bucketlist/create$',
        app_views.CreateBucketlist, name="create_bucketlist"),
    url(r'^bucket/(?P<bucket_id>[0-9]+)/bucketlist/(?P<bucketlist_id>[0-9]+)/edit$',
        app_views.UpdateBucketlist,name="edit_bucketlist"),
    url(r'^bucket/(?P<bucket_id>[0-9]+)/bucketlist/(?P<bucketlist_id>[0-9]+)/delete$',
        app_views.DeleteBucketlist,name="delete_bucketlist"),
    url(r'^bucket/(?P<bucket_id>[0-9]+)/bucketlist/(?P<bucketlist_id>[0-9]+)/review/create$',
        app_views.CreateBucketlistReview,name="create_bucketlist_review"),
    url(r'^bucket/(?P<bucket_id>[0-9]+)/bucketlist/(?P<bucketlist_id>[0-9]+)/review/(?P<review_id>[0-9]+)/edit$',
        app_views.UpdateBucketlistReview,name="edit_bucketlist_review"),
    url(r'^bucket/(?P<bucket_id>[0-9]+)/bucketlist/(?P<bucketlist_id>[0-9]+)/review/(?P<review_id>[0-9]+)/delete$',
        app_views.DeleteBucketlistReview,name="delete_bucketlist_review"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
