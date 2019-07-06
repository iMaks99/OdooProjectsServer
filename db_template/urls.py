from django.urls import path
from . import views

urlpatterns = [
    path('connection/', views.db_connection),
]
