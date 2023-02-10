from django.db import models
from users.models import Profile
import uuid

class Language(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    language_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField('created')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.language_name

class LanguageExample(models.Model):
    language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField('created')

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = 'asdf'