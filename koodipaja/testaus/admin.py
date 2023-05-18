from django.contrib import admin
from .models import (Person, Group, Membership, MyModel)


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)


class GroupAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)


admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)

admin.site.register(MyModel)
