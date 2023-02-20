# def listLanguages(request):
#     context = {}
#     context['language'] = Language.objects.all()

#     return render(request, 'languages/list-languages.html', context)


# def listExamples(request):
#     example = LanguageExample.objects.all()
#     print(example)
#     context = {'example':example}
#     print(context)

#     return render(request, 'languages/language-examples.html', context)


# def viewSingleLanguage(request, pk):
    # instance = LanguageExample.objects.values_list('language', flat=True)
    # asdf = instance
    # print('print:', asdf)


# def listExamples(request):
#     profile = request.user.profile
#     print(profile)
#     example = profile.languageexample_set.all()
#     context = {'example':example}
#     print(context)

    # return render(request, 'languages/language-examples.html', context)