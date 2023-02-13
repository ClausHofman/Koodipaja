from django.shortcuts import render

# Create your views here.

def kotisivu(request):

    return render(request, 'main.html')