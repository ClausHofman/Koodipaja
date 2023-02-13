from django.shortcuts import render

# Create your views here.

def testingHomepage(request):
    return render(request, 'main_testing.html')