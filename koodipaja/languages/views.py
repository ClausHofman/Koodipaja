from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Language, LanguageExample
from users.models import Profile
from .forms import LanguageExampleForm

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
    profile = request.user.profile
    language = profile.language_set.get(languageexample__exact=f'{pk}')
    esimerkki = LanguageExample.objects.filter(id=pk)
    
    context = {'example':esimerkki, 'object':language}

    return render(request, 'languages/view-example.html', context)

def createLanguageExample(request, pk):
    form = LanguageExampleForm()

    if request.method == 'POST':
        form = LanguageExampleForm(request.POST)
        if form.is_valid():
            form.save()
                        
            return redirect('languages:view-language', pk)


    context = {'form':form}
    context['object'] = Language.objects.get(id=pk)
    return render(request, "languages/languageexample_form.html", context)

# def createLanguageExample(request):
#     form = LanguageExampleForm()

#     if request.method == 'POST':
#         form = LanguageExampleForm(request.POST)
#         if form.is_valid():
#             form.save()
                        
#             return redirect('languages:language-list')


#     context = {'form':form}
#     return render(request, "languages/languageexample_form.html", context)
