from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.core import serializers
from .models import PostBase

class HomePageView(TemplateView):

        template_name="home.html"
        latest_post = PostBase.objects.none()
        tmp = PostBase.objects.none()

        
        def get(self, *args,**kwargs):

                context=super().get_context_data(**kwargs)
                selection=self.request.GET.get('selection')
                context['is_superuser'] = self.request.user.is_superuser
                
                if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
                        if selection == "All":
                                latest_post=PostBase.objects.order_by('-id')[:4]
                                
                        elif selection == "Travel":
                                latest_post=PostBase.objects.order_by('-id').filter(category="Travel")[:4]

                        elif selection == "Projects":
                                latest_post=PostBase.objects.order_by('-id').filter(category="Project")[:4]
                        
                        elif selection == "Blogs":
                                latest_post=PostBase.objects.order_by('-id').filter(category="Blogs")[:4]
                
                        elif selection == "Photos":
                                latest_post=PostBase.objects.order_by('-id').filter(category="Photos")[:4]

                        print(latest_post)
                        finaljson = serializers.serialize('json',latest_post)
                        return JsonResponse(finaljson,safe=False)        
                        
                
                else:
                        latest_post=PostBase.objects.order_by('-id')[:4]
                        context['posts']=latest_post
                        print(self.request.user.is_superuser)
                        return self.render_to_response(context)