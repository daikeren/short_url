from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import LinkObjectApiView

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^api/(?P<pk>\d+)/?$', LinkObjectApiView.as_view(),
        name='url_shortener_api'),
)
