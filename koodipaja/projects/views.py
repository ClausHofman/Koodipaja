from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from users.models import Profile
from .models import Project, ProjectPage, ProjectPageTitle, ProjectArticle
from .forms import (ProjectForm, ProjectTagForm, ProjectPageForm, ProjectArticleForm,
                    ProjectPageTagForm, ProjectPageTitleForm)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .utils import searchProjects, paginateProjects, utils_search_articles, utils_search_titles


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
    my_object = get_object_or_404(ProjectArticle, pk=pk)
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Toggle the BooleanField value
        my_object.favorite = not my_object.favorite
        my_object.save()

        return JsonResponse({'my_boolean_field': my_object.favorite})

    profile = request.user.profile
    article_title = profile.projectarticle_set.get(id=pk)

    context = {'article_title': article_title, 'my_object': my_object}
    context['object2'] = ProjectPageTitle.objects.get(projectarticle__id=pk)

    return render(request, 'projects/view-article-title.html', context)


# FORMS

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
