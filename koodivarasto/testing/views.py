from django.shortcuts import render
from users.models import Profile
from languages.models import Language, LanguageExample

# Create your views here.

def testingHomepage(request):
    return render(request, 'main_testing.html')

def viewTest1(request, pk):
    profile = Profile.objects.get(id=pk)

    context = {'profile':profile}
    return render(request, 'testing/test-views-1.html', context)

def viewTest2(request, pk):
    profile = Profile.objects.get(id=pk)

    context = {'profile':profile}
    return render(request, 'testing/test-views-2.html', context)

def test_listLanguages(request):
    # get the user profile using request (user-profile one-to-one relationship)
    profile = request.user.profile
    print(profile)
    language = profile.language_set.all()
    print(language)

    context = {'profile':profile, 'language':language}
    print(context)
    return render(request, 'test_languages/test-list-languages.html', context)