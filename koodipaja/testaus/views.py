from django.shortcuts import render, get_object_or_404
from users.models import Profile
from languages.models import Language, LanguageExample
from .models import MyModel
from django.http import JsonResponse

# Create your views here.


def testingHomepage(request):
    return render(request, 'main_testing.html')


def viewTest1(request, pk):
    profile = Profile.objects.get(id=pk)

    context = {'profile': profile}
    return render(request, 'testing/test-views-1.html', context)


def viewTest2(request, pk):
    profile = Profile.objects.get(id=pk)

    context = {'profile': profile}
    return render(request, 'testing/test-views-2.html', context)


def toggle_boolean(request, pk):
    my_object = get_object_or_404(MyModel, pk=pk)

    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Toggle the BooleanField value
        my_object.my_boolean_field = not my_object.my_boolean_field
        my_object.save()

        return JsonResponse({'my_boolean_field': my_object.my_boolean_field})

    # Render the template for normal page rendering
    return render(request, 'testing/my_template.html', {'my_object': my_object})
