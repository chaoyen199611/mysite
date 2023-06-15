from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import TravelPost,TravelPostSection


class TravelPageView(TemplateView):

    template_name="travel.html"
    
    def get_context_data(self, *args,**kwargs):
            context=super().get_context_data(*args,**kwargs)
            context['travels'] = TravelPost.objects.all()
            return context
    
class TravelDetailView(TemplateView):

    template_name="travel_detail.html"

    def get_context_data(self, *args,**kwargs):
        
        context=super().get_context_data(*args,**kwargs)
        travel = TravelPost.objects.get(pk=kwargs.get('pk'))
        context['travelMain']= travel
        context['sections']=TravelPostSection.objects.filter(belongPost=kwargs.get('pk'))
        return context