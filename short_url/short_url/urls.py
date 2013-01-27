from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='short_url/index.html'),
        name='home'),
    url(r'^short_url/', include('url_shortener.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
