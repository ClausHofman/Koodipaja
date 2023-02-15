from django.http import HttpResponse
from django.shortcuts import render
from .models import Language, LanguageExample

def languagesIndex(request):
    return HttpResponse("Hello, world. You're at the languages index.")

def listLanguages(request):
    context = {}
    context['language'] = Language.objects.all()

    return render(request, 'languages/list-languages.html', context)

def viewSingleLanguage(request, pk):
    viewSingleLanguageObj = Language.objects.get(id=pk)

    return render(request, 'languages/view-language.html', {'object':viewSingleLanguageObj})

def listExamples(request):
    example = LanguageExample.objects.all()
    context = {'example':example}
    print(context)

    return render(request, 'languages/language-examples.html', context)
