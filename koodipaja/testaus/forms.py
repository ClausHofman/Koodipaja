from django.forms import ModelForm
from .models import Malli1, Malli2, Muistipeli, ModelX


class MuistipeliForm(ModelForm):
    class Meta:
        model = Muistipeli
        fields = ['title']


class Malli1Form(ModelForm):
    class Meta:
        model = Malli1
        fields = ['owner', 'muistipeli', 'question', 'answer']


class Malli2Form(ModelForm):
    class Meta:
        model = Malli2
        fields = ['owner', 'muistipeli', 'question', 'answer']


class ModelXForm(ModelForm):
    class Meta:
        model = ModelX
        fields = ['name']
