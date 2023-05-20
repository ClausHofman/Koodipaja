from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from users.models import Profile
from projects.models import ProjectArticle
from .models import MyModel, Malli1, Malli2
from .forms import Malli1Form, Malli2Form, MuistipeliForm

# Create your views here.


def testingHomepage(request):
    return render(request, 'main_testing.html')


def testi_kysely(request):
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


@login_required(login_url='users:login')
def muistipeli(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        kikkare = profile.malli1_set.all()
    else:
        return redirect('users:login')

    context = {'kikkare': kikkare}
    return render(request, 'testing/muistipeli.html', context)


@login_required(login_url='users:login')
def new_muistipeli(request):

    form = MuistipeliForm()

    if request.method == 'POST':
        form = MuistipeliForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('testaus:muistipeli')

    context = {'form': form}

    return render(request, 'testing/muistipeli_form.html', context)


@login_required(login_url='users:login')
def create_malli1(request):

    form = Malli1Form()

    if request.method == 'POST':
        form = Malli1Form(request.POST)
        if form.is_valid():
            form.save()

            return redirect('testaus:muistipeli')

    context = {'form': form}

    return render(request, 'testing/malli1_form.html', context)
