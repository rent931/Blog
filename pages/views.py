from re import template
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/index.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"