from django import forms
from django.forms import ModelForm
# from django import forms
from .models import Project, ProjectTag, ProjectPage, ProjectPageTag, ProjectArticle, ProjectArticleTag


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['owner', 'title', 'body', 'tags']


class ProjectTagForm(ModelForm):
    class Meta:
        model = ProjectTag
        fields = ['name']


class ProjectPageForm(ModelForm):
    class Meta:
        model = ProjectPage
        fields = ['owner', 'project', 'title', 'page_number', 'tags']
        widgets = {
            'owner': forms.Select(),
            'project': forms.Select(),
        }


class ProjectPageTagForm(ModelForm):
    class Meta:
        model = ProjectPageTag
        fields = ['name']


class ProjectArticleForm(ModelForm):
    class Meta:
        model = ProjectArticle
        fields = ['owner', 'project', 'project_page', 'title', 'body', 'tags']
        widgets = {
            'owner': forms.Select(),
            'project': forms.Select(),
            'project_page': forms.Select(),
            'body': forms.Textarea(),
        }


class ProjectArticleTagForm(ModelForm):
    class Meta:
        model = ProjectArticleTag
        fields = ['name']
