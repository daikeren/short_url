import logging
import json

from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.conf import settings

from braces.views import JSONResponseMixin, AjaxResponseMixin
from .models import Link
from .forms import LinkForm

logger = logging.getLogger(__name__)


class LinkObjectApiView(JSONResponseMixin, SingleObjectMixin, View):
    model = Link
    slug_field = 'code'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        context_dict = {
            "url": instance.url,
            "clicks": instance.clicks,
            "created": instance.created,
            "updated": instance.updated
        }

        return self.render_json_response(context_dict)


class LinkObjectCreateApiView(JSONResponseMixin, View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(LinkObjectCreateApiView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.raw_post_data)
        form = LinkForm(data)
        if form.is_valid():
            instance = form.save()
            json_dict = {
                "url": instance.url,
                "short_url": settings.BASE_URL + instance.code
            }
            return self.render_json_response(json_dict)

        response = self.render_json_response(form.errors)
        response.status_code = 400
        return response


class LinkCreateView(AjaxResponseMixin, CreateView):
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

        logger.debug('The shorten URL of {url} is generated as {code}'
                     .format(**format_dict))

        return reverse('url_shortener_home')


def visitShortURL(request, code):
    link = get_object_or_404(Link, code=code)
    link.clicks += 1
    link.save()
    logger.debug('Code {code} visited. Real URL: {url}'
                 .format(code=code, url=link.url))
    return redirect(link.url)
