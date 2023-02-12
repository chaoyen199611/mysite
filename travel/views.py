from django.shortcuts import render
from django.views.generic.base import TemplateView


class TravelPageView(TemplateView):

    template_name="travel.html"
    
    def get_context_data(self, *args,**kwargs):
            context=super().get_context_data(*args,**kwargs)
            return context