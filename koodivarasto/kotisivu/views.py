from django.shortcuts import render

# Create your views here.

def kotisivu(request):

    return render(request, 'main.html')

def kotisivu_notes(request):
    return render(request, 'site_notes.html')