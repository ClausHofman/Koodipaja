from django.forms import ModelForm
# from django import forms
from .models import LanguageExample

class LanguageExampleForm(ModelForm):
    # needs to be imported into views
    class Meta:
        model = LanguageExample
        fields = ['owner', 'language', 'title', 'description', 'tags']
        