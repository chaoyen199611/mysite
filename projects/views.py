
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from .models import ProjectPost,ProjectPostSection
from .forms import ProjectForm
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
                for key in request.POST:
                    if key.startswith('field'):
                        field_value = request.POST[key]
                        print(field_value)
                print(form.cleaned_data["title"])
                print(form.cleaned_data["category"])

                return redirect('project-home')
        else:
                print(form.errors)
        
        return self.get(self.request, *args, **kwargs)
    
class ProjectDetailView(TemplateView):

    template_name="projects_detail.html"

    def get_context_data(self, *args,**kwargs):
        
        context=super().get_context_data(*args,**kwargs)
        project = ProjectPost.objects.get(pk=kwargs.get('pk'))
        context['projectMain']= project
        context['sections']=ProjectPostSection.objects.filter(belongPost=kwargs.get('pk'))
        return context