from django.urls import path
from . import views

urlpatterns = [
    path('getprojectsall/', views.get_projects_all),
    path('login/', views.login_user),
    path('getprojecttasks/', views.get_project_tasks),
    path('getprojecttasktype/', views.get_project_stages),
    path('getusertasks/', views.get_user_tasks),
    path('getusertasksstages/', views.get_user_tasks_stages),
    path('getdepartmentsall/', views.get_departments_all),
    path('getdepartmentemployees/', views.get_department_employees),
    path('getprojectbyid/', views.get_project_by_id),
    path('gettaskbyid/', views.get_task_by_id),
    path('getuser/', views.get_user),
    path('gettaskmailactivity/', views.get_task_mail_activity),
    path('getuserrespartners/', views.get_user_res_partners),
    path('getrespartnersall/', views.get_res_partners_all),
    path('gettasktagsall/', views.get_task_tags_all),

    path('addprojecttask/', views.add_project_task),
    path('deleteprojecttask/', views.delete_project_task),
    path('editprojecttask/', views.edit_project_task),

    path('createproject/', views.create_project),
    path('editproject/', views.edit_project),
    path('deleteproject/', views.delete_project),
]
