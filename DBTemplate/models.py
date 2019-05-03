from django.db import models


class Databases(models.Model):
    ENGINE = models.CharField(max_length=1000, blank=True, null=True)
    NAME = models.CharField(max_length=1000, blank=True, null=True)
    USER = models.CharField(max_length=1000, blank=True, null=True)
    PASSWORD = models.CharField(max_length=1000, blank=True, null=True)
    HOST = models.CharField(max_length=1000, blank=True, null=True)
    PORT = models.CharField(max_length=1000, blank=True, null=True)


class FCMUsers(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    fcm_token = models.CharField(max_length=1000, blank=True, null=True)
