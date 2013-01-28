from django.conf.urls import patterns, include, url
from django.contrib import admin

from url_shortener.views import LinkCreateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', LinkCreateView.as_view(),
        name='home'),
    url(r'^short_url/', include('url_shortener.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
