from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import LinkObjectApiView, visitShortURL, LinkCreateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', LinkCreateView.as_view(),
        name='url_shortener_home'),
    url(r'^(?P<code>[a-zA-Z0-9]{6})$', visitShortURL,
        name='url_shortener_visit'),
    url(r'^api/(?P<slug>[a-zA-Z0-9]{6})/?$', LinkObjectApiView.as_view(),
        name='url_shortener_api'),
)
