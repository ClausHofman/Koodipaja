from django.shortcuts import render, redirect
from users.models import Profile
from .models import Project, ProjectPage, ProjectArticle
from .forms import ProjectForm, ProjectTagForm, ProjectPageForm

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
    
    context['object'] = Project.objects.get(id=pk)

    return render(request, 'projects/view-single-project.html', context)

def viewProjectPage(request, pk):
    profile = request.user.profile
    project_articles = profile.projectarticle_set.filter(project_page__exact=f'{pk}')
    project = profile.project_set.get(projectpage__exact=f'{pk}')

    context = {'project_articles':project_articles, 'object':project}

    return render(request, 'projects/project-page.html', context)


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
    form = ProjectPageForm(initial={'owner':f'{profile}', 'project':f'{project}', 
                                    'page_number':f'{page_number}'})

    if request.method == 'POST':
        form = ProjectPageForm(request.POST)
        if form.is_valid():
            form.save()
                        
            return redirect('projects:view-single-project', pk)


    context = {'form':form}
    context['object'] = Project.objects.get(id=pk)
    return render(request, "projects/projectpage_form.html", context)

