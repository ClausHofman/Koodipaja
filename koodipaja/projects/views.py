from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from users.models import Profile
from .models import Project, ProjectPage, ProjectPageTitle, ProjectArticle
from .forms import (ProjectForm, ProjectTagForm, ProjectPageForm, ProjectArticleForm,
                    ProjectPageTagForm, ProjectPageTitleForm, UpdateProjectArticleForm)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import resolve
from .utils import searchProjects, paginateProjects, utils_search_articles, utils_search_titles
from urllib.parse import urlparse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProjectSerializer, ProjectPageTitleSerializer, ProjectArticleSerializer
from pprint import pprint

# API


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectPageTitleViewSet(viewsets.ModelViewSet):
    queryset = ProjectPageTitle.objects.all()
    serializer_class = ProjectPageTitleSerializer

class ProjectArticleViewSet(viewsets.ModelViewSet):
    queryset = ProjectArticle.objects.all()
    serializer_class = ProjectArticleSerializer
    
    @action(detail=True, methods=['get', 'put', 'patch', 'delete'])
    def update_and_delete(self, request, pk=None):
        # Your update and delete logic here
        return Response({'detail': 'Update and delete response'})
    
    # @action(detail=False, methods=['get'])
    # def custom_action(self, request, pk=None):
    #     # Your custom action logic here
    #     return Response({'detail': 'Custom action response'})

# Views

@login_required(login_url='users:login')
def search_articles(request):

    profile = request.user.profile

    # need to get the return values
    articles, search_query = utils_search_articles(request)

    custom_range, articles = paginateProjects(request, articles, 10)

    # removed 'paginator':paginator from context because using the custom range
    context = {
        'articles': articles, 'search_query': search_query, 'custom_range': custom_range,
        'profile': profile
    }

    # pprint(context)
    return render(request, 'projects/search_article_titles.html', context)


@login_required(login_url='users:login')
def search_titles(request):

    profile = request.user.profile

    # need to get the return values
    titles, search_query = utils_search_titles(request)

    custom_range, titles = paginateProjects(request, titles, 10)

    # removed 'paginator':paginator from context because using the custom range
    context = {
        'titles': titles, 'search_query': search_query, 'custom_range': custom_range,
        'profile': profile
    }

    # pprint(context)
    return render(request, 'projects/search_page_titles.html', context)

# Delete #
@login_required(login_url='users:login')
def delete_item(request, pk):
    # Get the query parameter
    from_page = request.GET.get('from')
    print(f"Query Parameter 'from': {from_page}")  # Debug

    if not from_page:
        return HttpResponseNotFound("Invalid or missing 'from' parameter.")

    if from_page == 'list-page-articles':
        # Handle deletion for articles
        page_title = get_object_or_404(ProjectPageTitle, projectarticle__id=pk)
        article_to_delete = get_object_or_404(ProjectArticle, id=pk)

        if request.method == 'POST':
            article_to_delete.delete()
            return redirect('projects:list-page-articles', pk=page_title.id)

        return render(request, 'delete.html', {'article_to_delete': article_to_delete, 'page': 'list-page-articles'})

    elif from_page == 'list-page-titles':
        # Handle deletion for page titles
        project_page = get_object_or_404(ProjectPage, projectpagetitle__id=pk)
        page_title_to_delete = get_object_or_404(ProjectPageTitle, id=pk)

        if request.method == 'POST':
            page_title_to_delete.delete()
            return redirect('projects:list-page-titles', pk=project_page.id)

        return render(request, 'delete.html', {'page_title_to_delete': page_title_to_delete, 'page': 'list-page-titles'})

    # Fallback for unsupported or invalid values
    return HttpResponseNotFound("Invalid delete action context.")

    
@login_required(login_url='users:login')
def listProjects(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        project = profile.project_set.all()
    else:
        return redirect('users:login')

    context = {'project': project}
    return render(request, 'projects/list-projects.html', context)


@login_required(login_url='users:login')
def viewSingleProject(request, pk):
    profile = request.user.profile
    project_pages = profile.projectpage_set.filter(project__id=pk)

    context = {'project_pages': project_pages}

    context['object'] = Project.objects.get(id=pk)
    # context['object2'] = Project.objects.get(id=pk)

    return render(request, 'projects/list-project-pages.html', context)


@login_required(login_url='users:login')
def viewProjectPage(request, pk):
    profile = request.user.profile
    page_titles = profile.projectpagetitle_set.filter(project_page__id=pk)

    context = {'page_titles': page_titles}
    context['object'] = ProjectPage.objects.get(id=pk)
    context['object2'] = Project.objects.get(projectpage__id=pk)

    return render(request, 'projects/list-page-titles.html', context)


@login_required(login_url='users:login')
def viewPageTitle(request, pk):
    profile = request.user.profile
    articles = profile.projectarticle_set.filter(article_title__id=pk)

    context = {'articles': articles}
    context['object'] = ProjectPageTitle.objects.get(id=pk)
    context['object2'] = ProjectPage.objects.get(projectpagetitle__id=pk)

    return render(request, 'projects/list-articles.html', context)


@login_required(login_url='users:login')
def viewArticleTitle(request, pk):
    profile = request.user.profile
    article_title = profile.projectarticle_set.get(id=pk)
    # pprint(ProjectArticle._meta.get_fields())
    

    # testing utils generate_url
    # print(generate_url('projects:view-article-title',pk))
    
    # article_object = get_object_or_404(ProjectArticle, pk=pk)
    if request.method == "POST":
        # Toggle the BooleanField value
        article_title.favorite = not article_title.favorite
        article_title.save()

        return redirect('projects:view-article-title', pk)

    context = {'article_title': article_title}
    context['object2'] = ProjectPageTitle.objects.get(projectarticle__id=pk)

    return render(request, 'projects/view-article-title.html', context)


# FORMS

@login_required(login_url='users:login')
def updateArticle(request, pk):
    instance = get_object_or_404(ProjectArticle, pk=pk)    
    page_title = ProjectPageTitle.objects.get(projectarticle__id=pk)
    if request.method == 'POST':
        form = UpdateProjectArticleForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('projects:list-page-articles', page_title.id)
    else:
        # context['object'] = ProjectArticle.objects.get(projectarticle__id=pk)     
        form = UpdateProjectArticleForm(instance=instance)
        context = {'form': form}
    return render(request, 'projects/updateprojectarticle_form.html', context)

@login_required(login_url='users:login')
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('projects:list-projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url='users:login')
def createProjectTag(request):
    form = ProjectTagForm()

    if request.method == 'POST':
        form = ProjectTagForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('projects:list-projects')

    context = {'form': form}
    return render(request, "projects/projecttag_form.html", context)


@login_required(login_url='users:login')
def createProjectPage(request, pk):
    profile = request.user.profile
    project = Project.objects.get(id=pk)
    # count_pages = len(ProjectPage.objects.filter(project__title__startswith='EKA'))
    count_pages = len(ProjectPage.objects.filter(project_id=pk))
    page_number = count_pages + 1
    page_title = str('Page '+f'{page_number}')
    form = ProjectPageForm(initial={'owner': profile, 'project': project,
                                    'page_number': page_number, 'title': f'{page_title}'})

    if request.method == 'POST':
        form = ProjectPageForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('projects:list-project-pages', pk)

    context = {'form': form}
    context['object'] = Project.objects.get(id=pk)
    return render(request, "projects/projectpage_form.html", context)


@login_required(login_url='users:login')
def createProjectPageTitle(request, pk):
    profile = request.user.profile
    project = Project.objects.get(projectpage__id=pk)
    project_page = ProjectPage.objects.get(id=pk)
    form = ProjectPageTitleForm(initial={'owner': profile, 'project': project,
                                         'project_page': project_page})

    if request.method == 'POST':
        form = ProjectPageTitleForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('projects:list-page-titles', pk)

    context = {'form': form}
    context['object'] = ProjectPage.objects.get(id=pk)
    return render(request, "projects/projectpagetitle_form.html", context)


@login_required(login_url='users:login')
def createProjectArticle(request, pk):
    profile = request.user.profile
    project = Project.objects.get(projectpagetitle__id=pk)
    page = ProjectPage.objects.get(projectpagetitle__id=pk)
    page_title = ProjectPageTitle.objects.get(id=pk)

    form = ProjectArticleForm(
        initial={'owner': profile, 'project': project, 'project_page': page,
                 'article_title': page_title})

    if request.method == 'POST':
        form = ProjectArticleForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('projects:list-page-articles', pk)

    context = {'form': form}
    # context['object'] = ProjectPage.objects.get(id=pk)
    return render(request, "projects/projectarticle_form.html", context)


@login_required(login_url='users:login')
def createProjectPageTag(request, pk):
    form = ProjectPageTagForm()

    if request.method == 'POST':
        form = ProjectPageTagForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('projects:list-project-pages', pk)

    context = {'form': form}
    context['object'] = Project.objects.get(id=pk)
    return render(request, "projects/projectpagetag_form.html", context)

# TESTING ETC

# def viewSingleProject(request, pk):
#     profile = request.user.profile
#     projects = profile.project_set.filter(id=pk) # jäin tähän # huom! go back etc dynaamisissa linkeissä id:n pitää olla sama!
#     project_pages = profile.projectpage_set.filter(project__id=pk)
#     project_articles = profile.projectarticle_set.filter(project__id=pk)
#     print(projects)
#     print(project_pages)
#     print(project_articles)
#     context = {'project_pages':project_pages, 'project_articles':project_articles, 'projects':projects}

#     context['object'] = Project.objects.get(id=pk)

#     return render(request, 'projects/list-project-pages.html', context)
