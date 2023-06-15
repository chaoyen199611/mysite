from django.urls import path

from . import views

urlpatterns = [
    path('',views.TravelPageView.as_view(),name='travel-page'),
    path('<int:pk>/',views.TravelDetailView.as_view(),name='travel-detail'),
]