import json
from datetime import datetime

from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pyfcm import FCMNotification

from DBTemplate.models import FCMUsers
from DatabaseConnection.models import ProjectProject, ResUsers, ProjectTask, ProjectFavoriteUserRel, \
    HrDepartment, HrEmployee, MailActivity, ProjectTags, ProjectTagsProjectTaskRel, ResPartner


def get_projects_all(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    projects = ProjectProject.objects.using(db_id).filter(active=True).select_related('partner')

    result = [{
        'id': p.id,
        'name': p.name,
        'partner_id': p.partner_id if p.partner else None,
        'partner_name': p.partner.display_name if p.partner else None,
        'color': p.color,
        'tasks_count': ProjectTask.objects.using(db_id).filter(project=p.id).filter(stage_id__in=[4, 5]).count(),
        'is_favourite': ProjectFavoriteUserRel.objects.using(db_id).filter(
            Q(project=p.id) & Q(user=user[0].id)).exists(),
        'label_tasks': p.label_tasks,
        'user_id': p.user.id if p.user else None,
        'user_name': p.user.name if p.user else None,
        'privacy_visibility': p.privacy_visibility
    } for p in projects]

    return JsonResponse(result, safe=False)


def get_project_tasks(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    tasks = ProjectTask.objects.using(db_id) \
        .filter(project=request.GET.get('project_id')) \
        .select_related('stage').select_related('user').select_related('partner')

    result = [{
        'id': t.id,
        'name': t.name,
        'kanban_state': t.kanban_state,
        'customer_id': t.partner.id if t.partner else None,
        'customer_display_name': t.partner.display_name if t.partner else None,
        'customer_email': t.partner.email if t.partner else None,
        'priority': t.priority,
        'date_deadline': t.date_deadline,
        'mail_activity_state': 0,
        'stage_id': t.stage.id,
        'color': t.color,
        'assigned_to': t.user.partner.name if t.user else "",
        'assigned_to_id': t.user.partner.id if t.user else -1
    } for t in tasks]

    return JsonResponse(result, safe=False)


@csrf_exempt
def add_project_task(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    data = json.loads(request.body)
    task = ProjectTask()

    task.active = True
    task.company = user[0].company
    task.name = data['name']
    task.priority = data['priority']
    task.user = ResUsers.objects.using(db_id).get(partner=data['assigned_to_id'])
    task.stage_id = data['stage_id']
    if 'project_name' in data.keys():
        task.project = ProjectProject.objects.using(db_id).get(name=data['project_name'])

    if 'kanban_state' in data.keys():
        task.kanban_state = data['kanban_state']

    if 'date_deadline' in data.keys():
        task.date_deadline = datetime.strptime(data['date_deadline'], '%b %d, %Y %H:%M:%S')
    task.save()

    ProjectTagsProjectTaskRel.objects.using(db_id).filter(project_task=data['id']).delete()

    if 'color' in data.keys():
        task.color = data['color']

    if 'customer_id' in data.keys():
        task.partner_id = data['customer_id']

    if 'customer_email' in data.keys():
        task.email_from = data['customer_email']

    if 'description' in data.keys():
        task.description = data['description']

    if 'stage_id' in data.keys():
        task.stage_id = data['stage_id']

    if 'tags' in data.keys():
        for tag in data['tags']:
            temp = ProjectTags.objects.using(db_id).get(pk=tag['id'])
            rel = ProjectTagsProjectTaskRel(project_task=task, project_tags=temp)
            rel.save()

    task_created_notification(task)
    return JsonResponse(task.id, safe=False)


def delete_project_task(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    task = ProjectTask.objects.using(db_id).get(pk=request.GET.get('task_id'))
    task.delete()
    return HttpResponse(content='', content_type='application/json', status=200, reason=None, charset=None)


@csrf_exempt
def edit_project_task(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    data = json.loads(request.body)
    task = ProjectTask.objects.using(db_id).get(pk=data['id'])
    task.name = data['name']
    task.priority = data['priority']
    task.user = ResUsers.objects.using(db_id).get(partner=data['assigned_to_id'])
    task.stage_id = data['stage_id']
    if 'project_name' in data.keys():
        task.project = ProjectProject.objects.using(db_id).get(name=data['project_name'])

    if 'kanban_state' in data.keys():
        task.kanban_state = data['kanban_state']

    if 'date_deadline' in data.keys():
        task.date_deadline = datetime.strptime(data['date_deadline'], '%b %d, %Y %H:%M:%S')
    task.save()

    ProjectTagsProjectTaskRel.objects.using(db_id).filter(project_task=data['id']).delete()

    if 'color' in data.keys():
        task.color = data['color']

    if 'customer_id' in data.keys():
        task.partner_id = data['customer_id']

    if 'customer_email' in data.keys():
        task.email_from = data['customer_email']

    if 'description' in data.keys():
        task.description = data['description']

    if 'stage_id' in data.keys():
        task.stage_id = data['stage_id']

    if 'tags' in data.keys():
        for tag in data['tags']:
            temp = ProjectTags.objects.using(db_id).get(pk=tag['id'])
            rel = ProjectTagsProjectTaskRel(project_task=task, project_tags=temp)
            rel.save()

    task_edited_notofication(task)
    return HttpResponse(content='', content_type='application/json', status=200, reason=None, charset=None)


def get_task_by_id(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    tasks = ProjectTask.objects.using(db_id).get(pk=request.GET.get('task_id'))
    result = {
        'id': tasks.id,
        'name': tasks.name,
        'kanban_state': tasks.kanban_state,
        'customer_id': tasks.partner.id if tasks.partner else None,
        'customer_display_name': tasks.partner.display_name if tasks.partner else None,
        'customer_email': tasks.partner.email if tasks.partner else None,
        'priority': tasks.priority,
        'date_deadline': tasks.date_deadline,
        'mail_activity_state': 0,
        'stage_id': tasks.stage.id,
        'description': tasks.description,
        'project_id': tasks.project.id,
        'project_name': tasks.project.name,
        'planned_hours': tasks.planned_hours,
        'assigned_to': tasks.user.partner.name if tasks.user else "",
        'assigned_to_id': tasks.user.partner.id if tasks.user else -1,
        'tags': list(tasks.project_task_tag.values())
    }
    return JsonResponse(result, safe=False)


def get_user_tasks(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    tasks = ProjectTask.objects.using(db_id) \
        .filter(active=True, user=list(user.values())[0]['id']) \
        .select_related('project').select_related('user').select_related('stage')

    result = [{
        'id': t.id,
        'name': t.name,
        'kanban_state': t.kanban_state,
        'customer_id': t.partner.id if t.partner else None,
        'customer_display_name': t.partner.display_name if t.partner else None,
        'customer_email': t.partner.email if t.partner else None,
        'priority': t.priority,
        'date_deadline': t.date_deadline,
        'mail_activity_state': 0,
        'stage_id': t.stage.id,
        'color': t.color,
        'assigned_to': t.user.partner.name if t.user else "",
        'assigned_to_id': t.user.partner.id if t.user else -1,
    } for t in tasks]

    return JsonResponse(result, safe=False)


def get_user_tasks_stages(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    tasks = ProjectTask.objects.using(db_id).filter(active=True, user=list(user.values())[0]['id']) \
        .select_related('stage')

    result = [{
        'id': t.stage_id,
        'name': t.stage.name
    } for t in tasks]

    return JsonResponse(result, safe=False)


def get_project_stages(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    pr_id = request.GET.get('project_id')

    result = list(ProjectProject.objects.using(db_id).get(id=pr_id).project_type_memb.values())

    return JsonResponse(result, safe=False)


def get_task_mail_activity(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    mail_activities = MailActivity.objects.using(db_id).filter(res_id=request.GET.get("task_id"), res_model=171) \
        .select_related('activity_type')

    result = [{
        'id': ma.id,
        'res_id': ma.res_id,
        'res_model': ma.res_model_0,
        'activity_type': ma.activity_type.name,
        'summary': ma.summary,
        'note': ma.note,
        'date_deadline': ma.date_deadline
    } for ma in mail_activities]
    return JsonResponse(result, safe=False)


def get_task_tags_all(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    tags = list(ProjectTags.objects.using(db_id).all().values())
    return JsonResponse(tags, safe=False)


def get_departments_all(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token).select_related('company')
    if not user.exists():
        raise PermissionDenied()

    departments = list(HrDepartment.objects.using(db_id).filter(company=user[0].company.id).values())
    return JsonResponse(departments, safe=False)


def get_department_employees(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token).select_related('company')
    if not user.exists():
        raise PermissionDenied()

    employees = HrEmployee.objects.using(db_id).filter(department=request.GET.get('department_id')).select_related(
        'job')

    result = [{
        'id': e.id,
        'name': e.name,
        'work_location': e.work_location,
        'job': e.job.name,
        'category': list(e.employee_category.values())
    } for e in employees]

    return JsonResponse(result, safe=False)


def get_user_res_partners(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token).select_related('company')
    if not user.exists():
        raise PermissionDenied()

    users = ResUsers.objects.using(db_id).filter(active=True, company=user[0].company).select_related('partner')

    result = [{
        'id': u.partner.id,
        'name': u.partner.name,
        'display_name': u.partner.display_name,
        'email': u.partner.email
    } for u in users]

    return JsonResponse(result, safe=False)


def get_res_partners_all(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token).select_related('company')
    if not user.exists():
        raise PermissionDenied()

    result = list(ResPartner.objects.using(db_id).all().values())
    return JsonResponse(result, safe=False)


@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return HttpResponseNotFound("Incorrect request method")

    user = ResUsers.objects.using(request.POST['db_name']).get(login=request.POST['user_mail'])

    token = user.password

    try:
        fcm_user = FCMUsers.objects.using('default').get(user_id=user.id)
        fcm_user.fcm_token = request.POST['fcm_token']
    except FCMUsers.DoesNotExist:
        new_fcm_user = FCMUsers(user_id=user.id, fcm_token=request.POST['fcm_token'])
        new_fcm_user.save()

    return JsonResponse(token, safe=False)


push_service = FCMNotification(
    api_key='AAAAqekrmVs:APA91bGH9H9c48nXsvpTLAnkxKFDDvyXG-AZaizo6hWxchz1fD8a7lkmSynGTtlpXiZEyT4cPTZvgGegkgVmPQUpL_ZAJZKDTyldjqMBEB-ngpSbvrRXDZlJFuboj3tnx8Rxa0zn0DfO')


def task_created_notification(task):
    try:
        token = FCMUsers.objects.using('default').get(user_id=task.user.id)
        registration_id = token.fcm_token
        message_title = "New task"
        message_body = "You have been assigned a new task %s" % task.name
        push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                          message_body=message_body)
    except FCMUsers.DoesNotExist:
        pass
    return HttpResponse(content='', content_type='application/json', status=200, reason=None, charset=None)


def task_edited_notofication(task):
    try:
        token = FCMUsers.objects.using('default').get(user_id=task.user.id)
        registration_id = token.fcm_token
        message_title = "Task edited"
        message_body = "%s has been edited" % task.name
        push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                          message_body=message_body)
    except FCMUsers.DoesNotExist:
        pass

    return HttpResponse(content='', content_type='application/json', status=200, reason=None, charset=None)
