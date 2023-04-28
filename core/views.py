from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.core import serializers
from .models import PostBase
from travel.models import TravelPost
from blog.models import BlogPost
from projects.models import ProjectPost
from photo.models import PhotoPost


class HomePageView(TemplateView):

        template_name="home.html"
        latest_post = PostBase.objects.none()
        tmp = PostBase.objects.none()

        def get(self, *args,**kwargs):

                context=super().get_context_data(**kwargs)
                selection=self.request.GET.get('selection')
                
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

                        #latest_post=list(latest_post)
                        # final = PostBase.objects.none()
                        # for i in range(len(latest_post)):
                        #         latest_post_id=latest_post[i][0]
                        #         latest_post_category=latest_post[i][1]
                        #         if latest_post_category == "Blog":
                        #                 tmp=BlogPost.objects.filter(id=latest_post_id)
                        #         elif latest_post_category == "Travel":
                        #                 tmp=TravelPost.objects.filter(id=latest_post_id)
                        #         elif latest_post_category == "Project":
                        #                 tmp=ProjectPost.objects.filter(id=latest_post_id)
                        #         elif latest_post_category == "Photo":
                        #                 tmp=PhotoPost.objects.filter(id=latest_post_id)
                                

                        #         final=final.union(tmp)
                        context['posts']=latest_post
                        return self.render_to_response(context)