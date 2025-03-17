from django import forms
from django.forms import ModelForm
# from django import forms
from .models import (Project, ProjectTag, ProjectPage, ProjectPageTag, ProjectArticle,
                     ProjectArticleTag, ProjectPageTitle)


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


class ProjectPageTitleForm(ModelForm):
    class Meta:
        model = ProjectPageTitle
        fields = ['owner', 'project', 'project_page', 'title']
        widgets = {
            'owner': forms.Select(),
            'project': forms.Select(),
            'project_page': forms.Select(),
        }


class ProjectPageTagForm(ModelForm):
    class Meta:
        model = ProjectPageTag
        fields = ['name']


class ProjectArticleForm(ModelForm):
    class Meta:
        model = ProjectArticle
        fields = ['owner', 'project', 'project_page',
                  'article_title', 'title', 'body', 'tags']
        widgets = {
            'owner': forms.Select(),
            'project': forms.Select(),
            'project_page': forms.Select(),
            'article_title': forms.Select(),
            'title':forms.TextInput(attrs={'size': 147}),
            'body': forms.Textarea(attrs={'rows': 50, 'cols': 150}),
        }


class UpdateProjectArticleForm(ModelForm):
    class Meta:
        model = ProjectArticle
        fields = ['title', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'rows':50, 'cols': 150}),
            'title':forms.TextInput(attrs={'size': 147}),
        }


class ProjectArticleTagForm(ModelForm):
    class Meta:
        model = ProjectArticleTag
        fields = ['name']
