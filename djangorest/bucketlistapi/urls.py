from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^bucketlist/$',
        views.BucketlistView.as_view(),
        name="bucketlists"
    ),
    url(r'^bucketlist/(?P<bucketlist_id>[0-9]+)/$',
        views.BucketlistDetailView.as_view(),
        name="bucketlist"
    ),
    url(r'^bucketlist/(?P<bucketlist_id>[0-9]+)/reviews/$',
        views.ReviewListView.as_view()
    ),
    url(r'^bucketlist/(?P<bucketlist_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/$',
        views.ReviewDetailView.as_view()
    ),
}

urlpatterns = format_suffix_patterns(urlpatterns)
