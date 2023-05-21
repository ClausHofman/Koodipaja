from json import dumps
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


# Muistipeli

@login_required(login_url='users:login')
def muistipeli(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        kikkare = profile.malli1_set.all()

        kikkare2 = profile.malli2_set.all()
    else:
        return redirect('users:login')

    context = {'kikkare': kikkare, 'kikkare2': kikkare2}
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


def move_question_to_active(request, pk):
    model1_instance = Malli1.objects.get(id=pk)
    initial_values = {
        'owner': model1_instance.owner,
        'muistipeli': model1_instance.muistipeli,
        'question': model1_instance.question,
        'answer': model1_instance.answer
    }

    if request.method == 'POST':
        form = Malli1Form(request.POST)
        if form.is_valid():
            # Create a new instance of Model2 and copy the data from Model1
            model2_instance = Malli2(
                owner=form.cleaned_data['owner'],
                muistipeli=form.cleaned_data['muistipeli'],
                question=form.cleaned_data['question'],
                answer=form.cleaned_data['answer'],
                # Copy more fields from Model1 as needed
            )
            model2_instance.save()

            # Delete the original Model1 instance
            model1_instance.delete()

            # Redirect to a success view after successful submission
            return redirect('testaus:muistipeli')
    else:
        form = Malli1Form(initial=initial_values)

    context = {'form': form}

    return render(request, 'testing/active_question_form.html', context)


def move_question_to_inactive(request, pk):
    model2_instance = Malli2.objects.get(id=pk)
    initial_values = {
        'owner': model2_instance.owner,
        'muistipeli': model2_instance.muistipeli,
        'question': model2_instance.question,
        'answer': model2_instance.answer
    }

    if request.method == 'POST':
        form = Malli2Form(request.POST)
        if form.is_valid():
            # Create a new instance of Model2 and copy the data from Model1
            model1_instance = Malli1(
                owner=form.cleaned_data['owner'],
                muistipeli=form.cleaned_data['muistipeli'],
                question=form.cleaned_data['question'],
                answer=form.cleaned_data['answer'],
                # Copy more fields from Model1 as needed
            )
            model1_instance.save()

            # Delete the original Model1 instance
            model2_instance.delete()

            # Redirect to a success view after successful submission
            return redirect('testaus:muistipeli')
    else:
        form = Malli2Form(initial=initial_values)

    context = {'form': form}

    return render(request, 'testing/inactive_question_form.html', context)

# geeksforgeeks example


def send_dictionary(request):
    # create data dictionary
    mallit = Malli1.objects.all()

    my_objects_dict = []

    for obj in mallit:
        print(obj)
        obj_dict = {
            'question': obj.question,
            'answer': obj.answer
        }

        # Append the dictionary to the list
        my_objects_dict.append(obj_dict)

    # context = {'my_objects_dict': my_objects_dict}

    # dump data
    try:
        dataJSON = dumps(my_objects_dict[0])
        return render(request, 'testing/landing.html', {'data': dataJSON})
    except:
        return render(request, 'testing/landing.html')
