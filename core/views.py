from django.shortcuts import render
from django.core.mail import EmailMessage, get_connection
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name="home.html"

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        return context