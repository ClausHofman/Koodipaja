from pprint import pprint
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.urls import conf
from .forms import CustomUserCreationForm
from .models import Profile
from projects.models import ProjectArticle
from testaus.models import Muistipeli


def loginUser(request):
    page = 'login'

    # first check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('kotisivu:kotisivu')

    if request.method == 'POST':
        # print(request.POST)
        # extract by form fields
        username = request.POST['username'].lower()
        password = request.POST['password']

        # check that the username exists in the database
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        # authenticate checks that the password matches the username and return either the
        # user instance or None
        user = authenticate(request, username=username, password=password)

        # run a check in case the authentication succeeds or fails
        if user is not None:
            # login function will create a session for the user in the database in the sessions table
            # and add that into our browser's cookies.
            login(request, user)
            # Review_login
            return redirect(request.GET['next'] if 'next' in request.GET else 'kotisivu:kotisivu')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    # delete the session
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('users:login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()

            # hold a temporary instance of the form and create a user object which we can modify.
            # we might not want usernames to be case sensitive, for example.
            user = form.save(commit=False)
            user.username = user.username.lower()  # could be done directly in the form also
            user.save()

            messages.success(request, 'User account was created!')

            # we have the user object already thanks to commit=False earlier
            # so we just need to login and redirect
            login(request, user)
            return redirect('projects:list-projects')

        # form was not valid
        else:
            messages.error(
                request, 'An error has occured during registration!')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    context = {'profile': profile}
    print(context)
    return render(request, 'users/user-profile.html', context)


@login_required(login_url='users:login')
def userAccount(request):

    my_model_instance = Muistipeli.objects.all()

    return render(request, 'users/account.html', {'my_model_instance': my_model_instance})


def show_favorite_articles(request):
    # articles = ProjectArticle.objects.filter(favorite=True)
    # context = {'articles': articles}
    pass
