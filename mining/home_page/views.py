from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib import messages
from braces.views import MessageMixin

class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(MessageMixin, TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        self.messages.info("Site under construction")
        return super(HomePage, self).get(request, *args, **kwargs)
