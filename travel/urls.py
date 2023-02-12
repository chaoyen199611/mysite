from django.urls import path

from . import views

urlpatterns = [
    path('',views.TravelPageView.as_view(),name='travel-page')
]