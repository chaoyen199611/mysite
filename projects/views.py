
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from .models import ProjectPost
from .forms import ProjectForm
import datetime
from datetime import date
from django.http import JsonResponse


class ProjectPageView(TemplateView):

    template_name="projects.html"
    
    def get(self, *args,**kwargs):
        context=super().get_context_data(**kwargs)

        context['is_superuser'] = self.request.user.is_superuser
        context['projects'] = ProjectPost.objects.all()
        context['form'] = ProjectForm(initial={'category':'Project'})

        return self.render_to_response(context)
    
    def post(self,request, *args, **kwargs):
        
        form = ProjectForm(request.POST,request.FILES)  
        print(form.fields)
        if form.is_valid():
                instance = ProjectPost(
                    title = form.cleaned_data["title"],
                    category = form.cleaned_data["category"],
                    description = form.cleaned_data["description"],
                    post_time = date.today(),
                    thumbnail = form.cleaned_data["thumbnail"],
                    topic = form.cleaned_data["topic"],
                    image = form.cleaned_data["image"],
                    maincontent = form.cleaned_data["maincontent"]
                )
                instance.save()
                return redirect('project-home')
        else:
                print(form.errors)
        
        return self.get(self.request, *args, **kwargs)
    
class ProjectDetailView(TemplateView):

    template_name="projects_detail.html"

    def get_context_data(self, *args,**kwargs):
        
        context=super().get_context_data(*args,**kwargs)
        context['project']= ProjectPost.objects.get(pk=kwargs.get('pk'))

        return context