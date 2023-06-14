from django.shortcuts import render


from django.views.generic.base import TemplateView


class PhotoPageView(TemplateView):

    template_name="photo.html"

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        return context