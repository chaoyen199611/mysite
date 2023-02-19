from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import ProjectPost,ProjectPostSection


class ProjectPageView(TemplateView):

    template_name="projects.html"
    
    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)

        context['projects'] = ProjectPost.objects.all()
        return context
    
class ProjectDetailView(TemplateView):

    template_name="projects_detail.html"

    def get_context_data(self, *args,**kwargs):
        
        context=super().get_context_data(*args,**kwargs)
        project = ProjectPost.objects.get(pk=kwargs.get('pk'))
        context['projectMain']= project
        context['sections']=ProjectPostSection.objects.filter(belongPost=kwargs.get('pk'))
        return context