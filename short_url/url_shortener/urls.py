from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import LinkObjectApiView, visitShortURL

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^(?P<code>[a-zA-Z0-9]{6})$', visitShortURL,
        name='url_shortener_visit'),
    url(r'^api/(?P<pk>\d+)/?$', LinkObjectApiView.as_view(),
        name='url_shortener_api'),
)
