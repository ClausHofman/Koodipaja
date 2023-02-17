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


def kysely3(request, pk):
    muuttuja = Language.objects.get(id=pk)
    context = {'kysely':muuttuja}
    return render(request, 'tktutkija/kysely3.html', context)