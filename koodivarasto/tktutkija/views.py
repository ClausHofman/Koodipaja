from django.shortcuts import render
from languages.models import Language, LanguageExample
from users.models import Profile

# Create your views here.

def tktIndex(request):

    return render(request, 'tktutkija/tkt_index.html')


def kysely1(request):
    kysely = Language.objects.all()
    print(kysely)
    kysely2 = LanguageExample.objects.all()
    print(kysely2)
    profile = request.user.profile
    kysely3 = profile.language_set.all()
    print(kysely3)

    return render(request, 'tktutkija/kysely1.html', {
        'kysely': kysely, 'kysely2':kysely2, 'kysely3':kysely3
        })


def kysely2(request):
    profile = request.user.profile
    muuttuja = profile.language_set.all()

    context = {'profile':profile, 'kysely':muuttuja}

    return render(request, 'tktutkija/kysely2.html', context)


def kysely3(request, pk): #viimeks
    # kieli = Language.objects.get(id=pk)
    muuttuja = LanguageExample.objects.filter(language__exact=f'{pk}')
    muuttuja_list = []
    for x in muuttuja:
        muuttuja_list.append(x)
    # x = muuttuja.values_list('id', flat=True)
    print(muuttuja_list)   
    context = {'kysely':muuttuja_list}

    return render(request, 'tktutkija/kysely3.html', context)

# def kysely4(request, pk2):
#     muuttuja = LanguageExample.objects.get(id=pk2)
#     context = {'kysely':muuttuja}
#     return render(request, 'tktutkija/kysely4.html', context)

# def kysely4(request):
#     muuttuja = LanguageExample.objects.filter(language__exact='8e69caa4-26b4-4f10-995d-693b333e51ff')
#     return render(request, 'tktutkija/kysely3.html', {'kysely':muuttuja})