from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.db import connections, OperationalError
from django.views.decorators.csrf import csrf_exempt
from passlib.context import CryptContext

from DatabaseConnection.models import ProjectProject, ResUsers, ResPartner, ProjectTask, ProjectFavoriteUserRel


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
        'is_favourite': ProjectFavoriteUserRel.objects.using(db_id).filter(Q(project=p.id) & Q(user=user[0].id)).exists()
    } for p in projects]

    return JsonResponse(result, safe=False)


@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return HttpResponseNotFound("Incorrect request method")

    token = ResUsers.objects.using(request.POST['db_name']).get(login=request.POST['user_mail']).password
    return JsonResponse(token, safe=False)
