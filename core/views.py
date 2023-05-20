from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.core import serializers
from .models import PostBase
from .forms import BaseForm
from datetime import date
from projects.models import ProjectPost

class HomePageView(TemplateView):

        template_name="home.html"
        latest_post = PostBase.objects.none()
        tmp = PostBase.objects.none()

        
        
        def get(self, *args,**kwargs):

                context=super().get_context_data(**kwargs)
                context['is_superuser'] = self.request.user.is_superuser
                selection=self.request.GET.get('selection')
                category=self.request.GET.get('category')

                if selection !=None:
                          
                        if selection == "All":
                                latest_post=PostBase.objects.order_by('-id')[:4]      
                        elif selection == "Travel":
                                latest_post=PostBase.objects.order_by('-id').filter(category="Travel")[:4]
                        elif selection == "Projects":
                                latest_post=PostBase.objects.order_by('-id').filter(category="Project")[:4]
                        elif selection == "Blogs":
                                latest_post=PostBase.objects.order_by('-id').filter(category="Blog")[:4]
                        elif selection == "Photos":
                                latest_post=PostBase.objects.order_by('-id').filter(category="Photos")[:4]

                        print(latest_post)
                        finaljson = serializers.serialize('json',latest_post)
                        return JsonResponse(finaljson,safe=False)        

                elif category != None:
                        if category == 'Project':
                                additional_fields_html = render_to_string('../templates/form_templates/project_additional_fields.html')

                        return JsonResponse({'additional_fields': additional_fields_html})  
                
                else:
                        latest_post=PostBase.objects.order_by('-id')[:4]
                        context['posts']=latest_post
                        context['form'] = BaseForm(initial={'category':'Blog'})

                        return self.render_to_response(context)
                
        def post(self,request, *args, **kwargs):
        # Access the submitted form data
                
                form = BaseForm(request.POST,request.FILES)  
                if form.is_valid():
                # <process form cleaned data>
                        print(form.cleaned_data["title"])
                        print(form.cleaned_data["category"])
                        if form.cleaned_data["category"] == "Project":
                                instance = ProjectPost(
                                        title=form.cleaned_data['title'],
                                        category=form.cleaned_data['category'],
                                        description=form.cleaned_data['category'],
                                        just_test = form.cleaned_data['form_project_justtest'],
                                        topic = form.cleaned_data['topic'],
                                        post_time = date.today()
                                )
                                if 'thumbnail' in request.FILES:
                                        instance.thumbnail = request.FILES['thumbnail']
                                
                                instance.save()
                        
                        return redirect('home-page')
                else:
                        print(form.errors)
                
                return self.get(self.request, *args, **kwargs)