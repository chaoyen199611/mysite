from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.forms import modelform_factory
from django.http import JsonResponse
from django.core import serializers
from .models import PostBase,BaseForm
from projects.models import ProjectPost
from datetime import date



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
                        print(category)   
                        finaljson ={'foo':'bar'}
                        return JsonResponse(finaljson,safe=False)  
                
                else:
                        latest_post=PostBase.objects.order_by('-id')[:4]
                        context['posts']=latest_post
                        context['form'] = BaseForm()
                        print(self.request.user.is_superuser)
                        return self.render_to_response(context)
                
        def post(self,request, *args, **kwargs):
        # Access the submitted form data
                
                form = BaseForm(request.POST,request.FILES)  
                if form.is_valid():
                # <process form cleaned data>
                        print(form.cleaned_data["title"])
                        print(form.cleaned_data["category"])
                        if form.cleaned_data["category"] == "Blog":
                                instance = form.save(commit=False)
                                if 'thumbnail' in request.FILES:
                                        print(7777)
                                        instance.thumbnail = request.FILES['thumbnail']
                                instance.post_time = date.today()
                                instance.save()
                        
                        return redirect('home-page')
                else:
                        print(form.errors)
                
                return self.get(self.request, *args, **kwargs)