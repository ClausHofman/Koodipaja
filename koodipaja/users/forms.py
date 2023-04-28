from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

        # customize the field labels
        labels = {
            'first_name': 'Name'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # the field(s) we want to modify
        # self.fields['title'].widget.attrs.update({'class':'input', # CSS class, not Python class.
        #                                         'placeholder':'Add title'})
        # self.fields['description'].widget.attrs.update({'class':'input'}) # _form.css line 43 is the class in question

        # do it with a for loop
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location',
                  'bio', 'short_intro', 'social_github', 'social_linkedin',
                  'social_twitter', 'social_youtube', 'social_website']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


# class SkillForm(ModelForm):
#     class Meta:
#         model = Skill
#         fields ='__all__'
#         exclude = ['owner']

#     def __init__(self, *args, **kwargs):
#         super(SkillForm, self).__init__(*args, **kwargs)

#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'input'})


# class MessageForm(ModelForm):
#     class Meta:
#         model = Message
#         fields = ['name', 'email', 'subject', 'body']


#     def __init__(self, *args, **kwargs):
#         super(MessageForm, self).__init__(*args, **kwargs)

#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'input'})
