from json import dumps
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import Profile
from projects.models import ProjectArticle
from .models import MyModel, Malli1, Malli2, QuestionAnswerPair, ModelX
from .forms import Malli1Form, Malli2Form, MuistipeliForm, ModelXForm
from rest_framework import viewsets
from pprint import pprint


def cards_test_page(request):
    # Render the template with the JavaScript file
    return render(request, 'testing/cards_test.html')

def get_data(request):
    # Retrieve data from the database
    question_answer_pairs = QuestionAnswerPair.objects.all()

    # Serialize the data to JSON
    serialized_data = [{'question': pair.question_text, 'answer': pair.answer_text} for pair in question_answer_pairs]
    print(serialized_data)

    # Return JSON response
    return JsonResponse(serialized_data, safe=False)

def test_modelx(request):
    stuff = ModelX.objects.all()

    context = {'stuff': stuff}

    return render(request, 'testing/empty_test_page copy.html', context)

# ModelX form
# TODO: Try to make each box clickable that spawns a correct modal/dialog that supports multiple desired operations. If/when that's done, maybe could try something funky with overflow-x at some point (check ideas.txt)
# check empty_test_page.html, empty_test_page copy.html, # empty_test_page copy 2.html, # empty_test_page copy 3.html
def add_model_x(request):
    if request.method == 'POST':
        form = ModelXForm(request.POST)
        if form.is_valid():
            form = form.save()

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    else:
        form = ModelXForm()

    return render(request, 'testing/modelx_form.html', {'form': form})



from .serializers import QuestionAnswerPairSerializer

# API
class QuestionAnswerPairViewSet(viewsets.ModelViewSet):
    queryset = QuestionAnswerPair.objects.all()
    serializer_class = QuestionAnswerPairSerializer

















################################################################

def testingHomepage(request):
    return render(request, 'main_testing.html')


def general_testing(request):
    questions = Malli2.objects.values('question')
    anwers = Malli2.objects.values('answer')

    lista = []
    sk = {}
    for x,y in zip(questions, anwers):
        sk['question'] = x['question']
        sk['answer'] = y['answer']
        lista.append(sk)
    # pprint(lista)
    
    context = {'questions':questions, 'answers':anwers}

    return render(request, 'testing/general_testing_page.html', context)


def empty_test_page(request):
    articles = ProjectArticle.objects.filter(favorite=True)

    context = {'articles': articles}

    return render(request, 'testing/empty_test_page.html', context)


def toggle_boolean(request, pk):
    my_object = get_object_or_404(MyModel, pk=pk)
    
    if request.method == "POST":
        # Toggle the BooleanField value
        my_object.my_boolean_field = not my_object.my_boolean_field
        my_object.save()

        return redirect('testaus:toggle-boolean', pk)

    # Render the template for normal page rendering
    return render(request, 'testing/my_template.html', {'my_object': my_object})


# Muistipeli

@login_required(login_url='users:login')
def muistipeli(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        malli1 = profile.malli1_set.all()

        malli2 = profile.malli2_set.all()
    else:
        return redirect('users:login')

    context = {'malli1': malli1, 'malli2': malli2}
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
    mallit = Malli2.objects.all()
    q_a_pairs = QuestionAnswerPair.objects.all()

    mallit_dict = []
    q_a_pair_dict = []

    for obj in mallit:
        obj_dict = {}
        obj_dict = {
            'question': obj.question,
            'answer': obj.answer
        }

        # Append the dictionary to the list
        mallit_dict.append(obj_dict)

    for obj in q_a_pairs:
        obj_dict = {}
        obj_dict = {
            'question': obj.question_text,
            'answer': obj.answer_text
        }

        # Append the dictionary to the list
        q_a_pair_dict.append(obj_dict)


    try:
        dataJSON = dumps(q_a_pair_dict)
        return render(request, 'testing/landing.html', {'data': dataJSON})
    except:
        return render(request, 'testing/landing.html')
