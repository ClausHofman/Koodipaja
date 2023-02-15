from django.shortcuts import render
from .models import Profile

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    context = {'profile':profile}
    print(context)
    return render(request, 'users/user-profile.html', context)