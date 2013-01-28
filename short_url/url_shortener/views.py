from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

from braces.views import JSONResponseMixin
from .models import Link


class LinkObjectApiView(JSONResponseMixin, SingleObjectMixin, View):
    model = Link

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        context_dict = {
            "url": instance.url,
            "clicks": instance.clicks,
            "created": instance.created,
            "updated": instance.updated
        }

        return self.render_json_response(context_dict)


def visitShortURL(request, code):
    link = get_object_or_404(Link, code=code)
    link.clicks += 1
    link.save()

    return redirect(link.url)
