from django.urls import path
from . import views

urlpatterns = [
    path('connection/', views.db_connection),
    path('getProjectsAll/', views.get_projects_all),
    path('login/', views.login_user),
]
