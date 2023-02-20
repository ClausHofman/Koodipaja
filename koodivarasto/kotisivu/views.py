from django.shortcuts import render

# Create your views here.

def kotisivu(request):
    page = 'kotisivu'
    context = {'page':page}

    return render(request, 'main.html', context)

def kotisivu_notes(request):
    return render(request, 'site_notes.html')