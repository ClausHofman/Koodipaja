from django.http import HttpResponse
from django.shortcuts import render
from .models import Language, LanguageExample


def viewSingleLanguage(request, pk):
    
    context = {}
    context['object'] = Language.objects.get(id=pk)
    print(context)
    context['title'] = LanguageExample.objects.filter(language=pk)
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
