from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin

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


def api(request):

    pass
