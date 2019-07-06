from django.db import connections, OperationalError
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from db_template.models import Databases


@csrf_exempt
def db_connection(request):
    if request.method != "POST":
        return HttpResponseNotFound("Incorrect request method")

    database_id = request.POST['db_name']
    databaseExist = Databases.objects.using('default').filter(NAME=database_id)

    if not databaseExist.exists():
        create_db = Databases()
        create_db.ENGINE = 'django.db.backends.postgresql'
        create_db.NAME = database_id
        create_db.USER = request.POST['db_user']
        create_db.PASSWORD = request.POST['db_password']
        create_db.HOST = request.POST['db_host']
        create_db.PORT = request.POST['db_port']
        create_db.save()

        newDatabase = {'id': database_id, 'ENGINE': 'django.db.backends.postgresql', 'NAME': database_id,
                       'USER': request.POST['db_user'], 'PASSWORD': request.POST['db_password'],
                       'HOST': request.POST['db_host'], 'PORT': request.POST['db_port']}
        return connect_to_db(database_id, newDatabase)

    else:
        return get_db_cred(database_id)


def connect_to_db(database_id, newDatabase):
    connections.databases[database_id] = newDatabase
    db_conn = connections[database_id]
    try:
        db_conn.cursor()
    except OperationalError:
        return HttpResponseBadRequest()
    else:
        return HttpResponse(content='', content_type='application/json', status=200, reason=None, charset=None)


def get_db_cred(database_id):
    db = Databases.objects.using('default').get(NAME=database_id)
    newDatabase = {'id': db.id, 'ENGINE': db.ENGINE, 'NAME': db.NAME, 'USER': db.USER,
                   'PASSWORD': db.PASSWORD, 'HOST': db.HOST, 'PORT': db.PORT}
    return connect_to_db(database_id, newDatabase)
