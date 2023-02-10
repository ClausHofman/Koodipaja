from django.contrib import admin
from .models import Framework, FrameworkExample
# Register your models here.

@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ["framework_name", "owner", "created"]

@admin.register(FrameworkExample)
class FrameworkExampleAdmin(admin.ModelAdmin):
    list_display = ["title", "created"]
    search_fields = ['description']
    class Meta:
        list_filter = ['-created']