from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import PostBase
from travel.models import TravelPost
from blog.models import BlogPost
from projects.models import ProjectPost
from photo.models import PhotoPost


class HomePageView(TemplateView):

    template_name="home.html"

    def get_context_data(self, *args,**kwargs):

                context=super().get_context_data(*args,**kwargs)
                latest_post=PostBase.objects.values_list('id','category').order_by('-id')[:4]
                
                latest_post=list(latest_post)
                latest_post.reverse()

                final = PostBase.objects.none()
                for i in range(len(latest_post)):
                        latest_post_id=latest_post[i][0]
                        latest_post_category=latest_post[i][1]
                        if latest_post_category == "Blog":
                                tmp=BlogPost.objects.filter(id=latest_post_id)
                        elif latest_post_category == "Travel":
                                tmp=TravelPost.objects.filter(id=latest_post_id)
                        elif latest_post_category == "Project":
                                tmp=ProjectPost.objects.filter(id=latest_post_id)
                        elif latest_post_category == "Photo":
                                tmp=PhotoPost.objects.filter(id=latest_post_id)
                        

                        final=final.union(tmp)
                context['posts']=final
                return context