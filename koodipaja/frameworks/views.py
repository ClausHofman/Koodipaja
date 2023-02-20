from django.shortcuts import render
from .models import Framework, FrameworkExample
from users.models import Profile


def viewSingleFramework(request, pk):
    profile = request.user.profile
    esimerkit = profile.frameworkexample_set.filter(framework__exact=f'{pk}')

    context = {'esimerkki': esimerkit}
    context['object'] = Framework.objects.get(id=pk)

    return render(request, 'frameworks/view-framework.html', context)


def listFrameworks(request):
    profile = request.user.profile
    framework = profile.framework_set.all()
    examples = FrameworkExample.objects.all()
    esimerkit = profile.frameworkexample_set.all()

    context = {'profile': profile, 'framework': framework,
               'example': examples, 'esimerkki': esimerkit}

    return render(request, 'frameworks/list-frameworks.html', context)


def viewSingleExample(request, pk):
    esimerkki = FrameworkExample.objects.filter(id=pk)

    context = {'example': esimerkki}

    return render(request, 'frameworks/view-example.html', context)
