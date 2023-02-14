from django.urls import path

from . import views

urlpatterns = [
    path('',views.PhotoPageView.as_view(),name='photo-page')
]