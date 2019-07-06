from django.urls import include, path

urlpatterns = [
    path('', include('odoo_db.urls')),
    path('', include('db_template.urls')),
]
