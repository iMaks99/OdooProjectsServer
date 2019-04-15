from django.urls import path
from . import views

urlpatterns = [
    path('connection/', views.db_connection),
    path('getprojectsall/', views.get_projects_all),
    path('login/', views.login_user),
    path('getprojecttasks/', views.get_project_tasks),
    path('getprojecttasktype/', views.get_project_stages),
    path('getpartnerimage/', views.get_partner_image),
    path('getusertasks/', views.get_user_tasks),
    path('getusertasksstages/', views.get_user_tasks_stages),
    path('getdepartmentsall/', views.get_departments_all),
    path('getdepartmentemployees/', views.get_department_employees),
]
