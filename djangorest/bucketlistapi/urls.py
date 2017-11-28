from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from .views import BucketCreateView, BucketView, BucketDeleteView, BucketUpdateView, BucketlistCreateView, BucketSingleRetriveView, BucketlistDeleteView,BucketlistSingleRetriveView,BucketlistUpdateView
urlpatterns = {
    url(r'^login/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^bucket/new$', BucketCreateView.as_view(), name="bucket_create"),
    url(r'^bucket/$', BucketView.as_view(), name="buckets"),
    url(r'^bucket/(?P<pk>[0-9]+)/$', BucketSingleRetriveView.as_view(), name="bucketlists"),
    url(r'^bucket/(?P<pk>[0-9]+)/edit$', BucketUpdateView.as_view(), name="bucket_edit"),
    url(r'^bucket/(?P<pk>[0-9]+)/delete$', BucketDeleteView.as_view(), name="bucket_delete"),
    url(r'^bucketlist/new$', BucketlistCreateView.as_view(), name="bucketlist_create"),
    url(r'^bucketlist/(?P<pk>[0-9]+)$', BucketlistSingleRetriveView.as_view(), name="bucketlist"),
    url(r'^bucketlist/(?P<pk>[0-9]+)/edit$', BucketlistUpdateView.as_view(), name="bucketlist_update"),
    url(r'^bucketlist/(?P<pk>[0-9]+)/delete$', BucketlistDeleteView.as_view(), name="bucketlist_delete"),

}

urlpatterns = format_suffix_patterns(urlpatterns)
