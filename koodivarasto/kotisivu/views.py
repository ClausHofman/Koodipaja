from django.shortcuts import render, redirect
import languages.models, frameworks.models

# Create your views here.

def kotisivu(request):

    return render(request, 'main.html')