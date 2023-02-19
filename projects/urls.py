from django.urls import path

from . import views

urlpatterns = [
    path('',views.ProjectPageView.as_view(),name='project-home'),
    path('<int:pk>/',views.ProjectDetailView.as_view(),name='project-detail'),
]