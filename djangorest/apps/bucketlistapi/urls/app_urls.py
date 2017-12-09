from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import app_views

urlpatterns = {
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
