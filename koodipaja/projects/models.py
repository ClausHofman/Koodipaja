from django.db import models
import uuid
from users.models import Profile

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('ProjectTag', blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class ProjectTodo(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('ProjectTodoTag', blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.title

class ProjectPage(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=500)
    page_number = models.IntegerField()
    tags = models.ManyToManyField('ProjectPageTag', blank=True)
    id = models.AutoField(primary_key=True, unique=True, editable=True)

    def __str__(self):
        return self.title

class ProjectArticle(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    project_page = models.ForeignKey(ProjectPage, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('ProjectArticleTag', blank=True)
    id = models.AutoField(unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class ProjectTag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class ProjectTodoTag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class ProjectPageTag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class ProjectArticleTag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name