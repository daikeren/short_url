from django.conf.urls import patterns, include, url
from django.contrib import admin

from url_shortener.views import LinkCreateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'', include('url_shortener.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
