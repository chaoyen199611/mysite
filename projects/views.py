from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import ProjectPost


class ProjectPageView(TemplateView):

    template_name="projects.html"

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        return context
    
class ProjectDetailView(TemplateView):

    template_name="projects_detail.html"

    def get_context_data(self, *args,**kwargs):
        
        context=super().get_context_data(*args,**kwargs)
        context['projectMain']=ProjectPost.objects.get(pk=kwargs.get('pk'))
        return context