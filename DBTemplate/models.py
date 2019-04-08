from django.db import models


class Databases(models.Model):
    name = models.CharField(max_length=150)
    host = models.CharField(max_length=150)
    port = models.CharField(max_length=150)
    user = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
