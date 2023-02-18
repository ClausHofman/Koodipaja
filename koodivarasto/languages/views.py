from django.http import HttpResponse
from django.shortcuts import render
from .models import Language, LanguageExample
from users.models import Profile

def viewSingleLanguage(request, pk):
    
    context = {}
    context['object'] = Language.objects.get(id=pk)
    print(context)
    context['title'] = LanguageExample.objects.filter(language=pk)
    context['created'] = LanguageExample.objects.filter(language=pk)
    print(context)

    return render(request, 'languages/view-language.html', context)


def listLanguages(request):
    # get the user profile using request (user-profile one-to-one relationship)
    profile = request.user.profile
    print(profile)
    language = profile.language_set.all()
    print(language)

    context = {'profile':profile, 'language':language}
    print(context)
    return render(request, 'languages/list-languages.html', context)


def viewSingleExample(request, pk):
    
    context = {}
    context['description'] = LanguageExample.objects.get(id=pk)
    # FIXME: Esimerkkien linkit ovat samat! 
    print(context)

    return render(request, 'languages/view-language.html', context)

