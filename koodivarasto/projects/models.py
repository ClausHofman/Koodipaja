from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_created = models.DateTimeField('created')


class ProjectTopic(models.Model):
    project = models.ForeignKey(Project, on_delete=models.RESTRICT)
    project_topic_name = models.CharField(max_length=200)