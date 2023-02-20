from django.http import HttpResponse
from django.shortcuts import render
from .models import Language, LanguageExample
from users.models import Profile

def viewSingleLanguage(request, pk):
    profile = request.user.profile
    esimerkit = profile.languageexample_set.filter(language__exact=f'{pk}')

    context = {'esimerkki':esimerkit}

    context['object'] = Language.objects.get(id=pk)
#     print(context)
#     context['title'] = LanguageExample.objects.filter(language=pk)
#     context['created'] = LanguageExample.objects.filter(language=pk)
#     print(context)

    return render(request, 'languages/view-language.html', context)


def listLanguages(request):
    # get the user profile using request (user-profile one-to-one relationship)
    profile = request.user.profile
    # print(profile)
    language = profile.language_set.all()
    # print(language)
    examples = LanguageExample.objects.all()
    esimerkit = profile.languageexample_set.all()
    # print(esimerkit)

    context = {'profile':profile, 'language':language, 'example':examples, 'esimerkki':esimerkit}
    # print(context)
    return render(request, 'languages/list-languages.html', context)


def viewSingleExample(request, pk):
    # profile = request.user.profile
    # esimerkki = profile.languageexample_set.filter(language__exact=f'{pk}')
    esimerkki = LanguageExample.objects.filter(id=pk)
    
    context = {'example':esimerkki}

    return render(request, 'languages/view-example.html', context)




# def viewSingleExample(request, pk):
#     profile = request.user.profile
#     esimerkit = profile.languageexample_set.filter(id=pk)


#     context = {'esimerkki':esimerkit}

#     return render(request, 'languages/view-language.html', context)
