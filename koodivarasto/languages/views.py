from django.http import HttpResponse


def projectIndex(request):
    return HttpResponse("Hello, world. You're at the languages index.")