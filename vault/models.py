from django.conf import settings
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.CharField(max_length=255)
    create_date = models.DateTimeField('date created', auto_now_add=True)
    modified_date = models.DateTimeField('date created', auto_now=True)

    def __unicode__(self):
        return self.name


class Secret(models.Model):
    project = models.ForeignKey(Project)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    last_user = "Barbie"
    secret_ref = 'barbican_generated_value'
    create_date = models.DateTimeField('date created', auto_now_add=True)
    modified_date = models.DateTimeField('date created', auto_now=True)

    def __unicode__(self):
        return self.description


class ProjectMember(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    project = models.ForeignKey(Project)
    create_date = models.DateTimeField('date created', auto_now_add=True)
    modified_date = models.DateTimeField('date created', auto_now=True)
