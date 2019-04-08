from django.urls import include, path

urlpatterns = [
    path('', include('DatabaseConnection.urls')),
    path('', include('DBTemplate.urls')),
]
