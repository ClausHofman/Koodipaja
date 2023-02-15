from django.http import HttpResponse
from django.shortcuts import render
from .models import Language, LanguageExample


def viewSingleLanguage(request, pk):
    viewSingleLanguageObj = Language.objects.get(id=pk)

    return render(request, 'languages/view-language.html', {'object':viewSingleLanguageObj})

def listExamples(request):
    example = LanguageExample.objects.all()
    context = {'example':example}
    print(context)

    return render(request, 'languages/language-examples.html', context)



def listLanguages(request):
    # get the user profile using request (user-profile one-to-one relationship)
    profile = request.user.profile
    language = profile.language_set.all()

    context = {'profile':profile, 'language':language}
    print(context)
    return render(request, 'languages/list-languages.html', context)