from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^', include('apps.bucketlistapi.urls')),

]
