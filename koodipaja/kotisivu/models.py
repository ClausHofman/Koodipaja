from django.db import models
import uuid
# Create your models here.

class SiteNote(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class SiteNoteInfo(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    site_note = models.ForeignKey(SiteNote, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
