from django.forms import ModelForm
from .models import Malli1, Malli2, Muistipeli


class MuistipeliForm(ModelForm):
    class Meta:
        model = Muistipeli
        fields = ['title']


class Malli1Form(ModelForm):
    class Meta:
        model = Malli1
        fields = ['muistipeli', 'question', 'answer']


class Malli2Form(ModelForm):
    class Meta:
        model = Malli2
        fields = ['muistipeli', 'question', 'answer']
