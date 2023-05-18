from django.shortcuts import render, get_object_or_404
from users.models import Profile
from projects.models import ProjectArticle
from .models import MyModel
from django.http import JsonResponse

# Create your views here.


def testingHomepage(request):
    return render(request, 'main_testing.html')


def testi_kysely(request):
    # TODO: maybe use this later
    articles = ProjectArticle.objects.filter(favorite=True)

    context = {'articles': articles}

    return render(request, 'testing/testi_kysely.html', context)


def toggle_boolean(request, pk):
    my_object = get_object_or_404(MyModel, pk=pk)

    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Toggle the BooleanField value
        my_object.my_boolean_field = not my_object.my_boolean_field
        my_object.save()

        return JsonResponse({'my_boolean_field': my_object.my_boolean_field})

    # Render the template for normal page rendering
    return render(request, 'testing/my_template.html', {'my_object': my_object})
