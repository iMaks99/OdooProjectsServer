from django.core.exceptions import PermissionDenied
from django.db import connections, OperationalError
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from DatabaseConnection.models import ProjectProject, ResUsers, ProjectTask, ProjectFavoriteUserRel, \
    IrAttachment


@csrf_exempt
def db_connection(request):
    if request.method != "POST":
        return HttpResponseNotFound("Incorrect request method")

    database_id = request.POST['db_name']
    newDatabase = {"id": database_id, 'ENGINE': 'django.db.backends.postgresql', 'NAME': database_id,
                   'USER': request.POST['db_user'], 'PASSWORD': request.POST['db_password'],
                   'HOST': request.POST['db_host'], 'PORT': request.POST['db_port']}

    connections.databases[database_id] = newDatabase

    db_conn = connections[database_id]
    try:
        db_conn.cursor()
    except OperationalError:
        return HttpResponseBadRequest()
    else:
        return HttpResponse(content='', content_type='application/json', status=200, reason=None, charset=None)


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
        'partner': p.partner.display_name if p.partner else None,
        'tasks_count': ProjectTask.objects.using(db_id).filter(project=p.id).filter(stage_id__in=[4, 5]).count(),
        'is_favourite': ProjectFavoriteUserRel.objects.using(db_id).filter(
            Q(project=p.id) & Q(user=user[0].id)).exists()
    } for p in projects]

    return JsonResponse(result, safe=False)


def get_project_tasks(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    tasks = ProjectTask.objects.using(db_id).filter(project=request.GET.get('project_id'))

    result = [{
        'id': t.id,
        'name': t.name,
        'kanban_state': t.kanban_state,
        'email_from': t.email_from,
        'priority': t.priority,
        'date_deadline': t.date_deadline,
        'mail_activity_state': 0,
        'stage_id': t.stage.id
    } for t in tasks]

    return JsonResponse(result, safe=False)


def get_user_tasks(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    tasks = ProjectTask.objects.using(db_id).filter(active=True, user=list(user.values())[0]['id'])

    result = [{
        'id': t.id,
        'name': t.name,
        'kanban_state': t.kanban_state,
        'email_from': t.email_from,
        'priority': t.priority,
        'date_deadline': t.date_deadline,
        'mail_activity_state': 0,
        'stage_id': t.stage.id
    } for t in tasks]

    return JsonResponse(result, safe=False)


def get_user_tasks_stages(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    tasks = ProjectTask.objects.using(db_id).filter(active=True, user=list(user.values())[0]['id']).select_related('stage')

    result = [{
        'id': t.stage_id,
        'name': t.stage.name
    } for t in tasks]

    return JsonResponse(result, safe=False)


def get_partner_image(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    token = token.replace('Bearer ', '')
    db_id = request.META.get('HTTP_DBNAME', None)
    user = ResUsers.objects.using(db_id).filter(password=token)
    if not user.exists():
        raise PermissionDenied()

    partner = ProjectTask.objects.using(db_id).get(pk=request.GET.get('task_id')).user.partner_id
    result = IrAttachment.objects.using(db_id).get(res_model='res.partner', res_field='image', res_id=partner)
    return HttpResponse(result.db_datas, content_type='application/{0}'.format(result.mimetype))


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


@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return HttpResponseNotFound("Incorrect request method")

    token = ResUsers.objects.using(request.POST['db_name']).get(login=request.POST['user_mail']).password
    return JsonResponse(token, safe=False)
