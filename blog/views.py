from django.shortcuts import render
from django.views.generic.base import TemplateView


class BlogPageView(TemplateView):

    template_name="blog.html"
    
    def get_context_data(self, *args,**kwargs):
            context=super().get_context_data(*args,**kwargs)
            return context