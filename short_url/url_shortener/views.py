import logging

from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.conf import settings

from braces.views import JSONResponseMixin
from .models import Link
from .forms import LinkForm

logger = logging.getLogger(__name__)


class LinkObjectApiView(JSONResponseMixin, SingleObjectMixin, View):
    model = Link

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(LinkObjectApiView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        context_dict = {
            "url": instance.url,
            "clicks": instance.clicks,
            "created": instance.created,
            "updated": instance.updated
        }

        return self.render_json_response(context_dict)


class LinkCreateView(CreateView):
    model = Link
    template_name = 'short_url/index.html'
    form_class = LinkForm

    def get_success_url(self):
        format_dict = {
            'code': self.object.code,
            'url': self.object.url,
            'base_url': settings.BASE_URL,
        }
        msg = 'The shorten URL of <a href="{url}">{url}</a> \
            is <a href="{base_url}{code}">{code}</a>'.format(**format_dict)
        messages.add_message(
            self.request, messages.INFO, msg)
        return reverse('url_shortener_home')


def visitShortURL(request, code):
    link = get_object_or_404(Link, code=code)
    link.clicks += 1
    link.save()

    return redirect(link.url)
