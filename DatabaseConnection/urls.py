from django.urls import path
from . import views

urlpatterns = [
    path('connection/', views.index),
    path('getProjectsAll/', views.get_projects_all),
]
