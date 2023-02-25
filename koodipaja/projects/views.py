from django.shortcuts import render, redirect
from users.models import Profile
from .models import Project, ProjectPage, ProjectArticle
from .forms import ProjectForm, ProjectTagForm, ProjectPageForm, ProjectArticleForm

def listProjects(request):
    profile = request.user.profile
    project = profile.project_set.all()
    print(project)

    context = {'project':project}
    return render(request, 'projects/list-projects.html', context)

def viewSingleProject(request, pk):
    profile = request.user.profile
    project_pages = profile.projectpage_set.filter(project__id=pk)

    context = {'project_pages':project_pages}
    
    context['object'] = Project.objects.get(id=pk)

    return render(request, 'projects/view-single-project.html', context)

def viewProjectPage(request, pk):
    profile = request.user.profile
    articles = profile.projectarticle_set.filter(project_page__id=pk)

    context = {'articles':articles}
    return render(request, 'projects/view-project-page.html', context)

# FORMS

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
                        
            return redirect('projects:list-projects')

    context = {'form':form}
    return render(request, "projects/project_form.html", context)

def createProjectTag(request):
    form = ProjectTagForm()

    if request.method == 'POST':
        form = ProjectTagForm(request.POST)
        if form.is_valid():
            form.save()
                        
            return redirect('projects:list-projects')

    context = {'form':form}
    return render(request, "projects/projecttag_form.html", context)

def createProjectPage(request, pk):
    profile = request.user.profile
    project = Project.objects.get(id=pk)
    # count_pages = len(ProjectPage.objects.filter(project__title__startswith='EKA'))
    count_pages = len(ProjectPage.objects.filter(project_id=pk))
    page_number = count_pages + 1
    form = ProjectPageForm(initial={'owner':profile, 'project':project, 
                                    'page_number':page_number})

    if request.method == 'POST':
        form = ProjectPageForm(request.POST)
        if form.is_valid():
            form.save()
                        
            return redirect('projects:view-single-project', pk)


    context = {'form':form}
    context['object'] = Project.objects.get(id=pk)
    return render(request, "projects/projectpage_form.html", context)









# def createProjectArticle(request, pk):
#     profile = request.user.profile
#     project = ProjectPage.objects.get(id=pk)
#     testi_kysely = ProjectPage.objects.all()
#     print(project)
#     print(testi_kysely)
#     # count_pages = len(ProjectPage.objects.filter(project__title__startswith='EKA'))
#     # project_page = ProjectPage.objects.get(id=pk)
#     # print(project_page)
#     form = ProjectArticleForm(initial={'owner':f'{profile}', 'project':f'{project}'})

#     if request.method == 'POST':
#         form = ProjectArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
                        
#             return redirect('projects:view-project-page', pk)


#     context = {'form':form, 'object':project}
#     return render(request, "projects/projectarticle_form.html", context)

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

#     return render(request, 'projects/view-single-project.html', context)
