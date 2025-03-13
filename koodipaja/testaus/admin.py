from django.contrib import admin
from .models import (Person, Group, Membership, MyModel,
                     Malli1, Malli2, Muistipeli, QuestionAnswerPair, ModelX)


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)


class GroupAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)


admin.site.register(ModelX)

admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)

admin.site.register(MyModel)

admin.site.register(Malli1)
admin.site.register(Malli2)
admin.site.register(Muistipeli)

admin.site.register(QuestionAnswerPair)