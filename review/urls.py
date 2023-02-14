from django.urls import path

from . import views

urlpatterns = [
    path('',views.ReviewPageView.as_view(),name='review-page')
]