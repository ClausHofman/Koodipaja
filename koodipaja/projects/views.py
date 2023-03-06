from django.shortcuts import render, redirect
from users.models import Profile
from .models import Project, ProjectPage, ProjectPageTitle
from .forms import (ProjectForm, ProjectTagForm, ProjectPageForm, ProjectArticleForm,
                    ProjectPageTagForm, ProjectPageTitleForm)


def listProjects(request):
    profile = request.user.profile
    project = profile.project_set.all()

    context = {'project': project}
    return render(request, 'projects/list-projects.html', context)


def viewSingleProject(request, pk):
    profile = request.user.profile
    project_pages = profile.projectpage_set.filter(project__id=pk)

    context = {'project_pages': project_pages}

    context['object'] = Project.objects.get(id=pk)
    # context['object2'] = Project.objects.get(id=pk)

    return render(request, 'projects/list-project-pages.html', context)


def viewProjectPage(request, pk):
    profile = request.user.profile
    page_titles = profile.projectpagetitle_set.filter(project_page__id=pk)

    context = {'page_titles': page_titles}
    context['object'] = ProjectPage.objects.get(id=pk)
    context['object2'] = Project.objects.get(projectpage__id=pk)

    return render(request, 'projects/list-page-titles.html', context)


def viewPageTitle(request, pk):
    profile = request.user.profile
    articles = profile.projectarticle_set.filter(article_title__id=pk)

    context = {'articles': articles}
    context['object'] = ProjectPageTitle.objects.get(id=pk)
    context['object2'] = ProjectPage.objects.get(projectpagetitle__id=pk)

    return render(request, 'projects/list-articles.html', context)


def viewArticleTitle(request, pk):
    profile = request.user.profile
    article_title = profile.projectarticle_set.get(id=pk)

    context = {'article_title': article_title}
    context['object2'] = ProjectPageTitle.objects.get(projectarticle__id=pk)

    return render(request, 'projects/view-article-title.html', context)


# FORMS


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('projects:list-projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def createProjectTag(request):
    form = ProjectTagForm()

    if request.method == 'POST':
        form = ProjectTagForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('projects:list-projects')

    context = {'form': form}
    return render(request, "projects/projecttag_form.html", context)


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
