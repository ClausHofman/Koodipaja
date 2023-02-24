from django.shortcuts import render, redirect
from users.models import Profile
from .models import Project, ProjectPage, ProjectArticle

def listProjects(request):
    profile = request.user.profile
    project = profile.project_set.all()
    print(project)

    context = {'project':project}
    return render(request, 'projects/list-projects.html', context)

def viewSingleProject(request, pk):
    profile = request.user.profile
    project_pages = profile.projectpage_set.filter(project__exact=f'{pk}')

    context = {'project_pages':project_pages}

    return render(request, 'projects/view-single-project.html', context)

def viewProjectPage(request, pk):
    profile = request.user.profile
    project_articles = profile.projectarticle_set.filter(project_page__exact=f'{pk}')
    project = profile.project_set.get(projectpage__exact=f'{pk}')

    context = {'project_articles':project_articles, 'object':project}

    return render(request, 'projects/project-page.html', context)
