from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse
from django.db import connections, OperationalError

from DatabaseConnection.models import ProjectProject, ResUsers


def index(request):
    database_id = 'coursework'
    newDatabase = {}
    newDatabase["id"] = database_id
    newDatabase['ENGINE'] = 'django.db.backends.postgresql'
    newDatabase['NAME'] = 'coursework'
    newDatabase['USER'] = 'openpg'
    newDatabase['PASSWORD'] = 'openpgpwd'
    newDatabase['HOST'] = 'localhost'
    newDatabase['PORT'] = '5432'
    connections.databases[database_id] = newDatabase

    db_conn = connections[database_id]
    try:
        c = db_conn.cursor()
    except OperationalError:
        connected = False
    else:
        connected = True

    users = list(ResUsers.objects.using('coursework').filter(login='maks.ismoilov0618@gmail.com').values('password'))

    return HttpResponse(connected)



def get_projects_all(request):
    index(request)
    token = ResUsers.objects.using('coursework').get(login='maks.ismoilov0618@gmail.com').password
    print(token)
    token1 = '$pbkdf2-sha512$25000$3dv7v1dqrTUmZEzJGUMo5Q$qt33iS1p4rmxjNkeqaC0n3o6MPm/A70x9s7xcWQo2pDVIukc6bMyVsAhbUAv6IMIW751SFDqTDkKVOifK.Bnag'

    if not ResUsers.objects.using('coursework').filter(password=token).exists():
         raise PermissionDenied()

    projects = list(ProjectProject.objects.using('coursework').values())
    return JsonResponse(projects, safe=False)
