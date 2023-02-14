from django.shortcuts import render
from django.views.generic.base import TemplateView


class ReviewPageView(TemplateView):

    template_name="review.html"
    
    def get_context_data(self, *args,**kwargs):
            context=super().get_context_data(*args,**kwargs)
            return context