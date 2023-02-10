from django.contrib import admin
from django.contrib import messages
from .models import State

class StateAdmin(admin.ModelAdmin):
	list_display = ('name', 'active', 'created_on')

	def active(self, obj):
		return obj.is_active == 1

	active.boolean = True

	def make_active(modeladmin, request, queryset):
		queryset.update(is_active = 1)
		messages.success(request, "Selected Record(s) Marked as Active Successfully !!")

	def make_inactive(modeladmin, request, queryset):
		queryset.update(is_active = 0)
		messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")

	admin.site.add_action(make_active, "Make Active")
	admin.site.add_action(make_inactive, "Make Inactive")

admin.site.register(State, StateAdmin)

# Disable delete option
# from django.contrib import admin
# from django.contrib import messages
# from .models import State

# class StateAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'active', 'created_on')

# 	def active(self, obj):
# 		return obj.is_active == 1

# 	active.boolean = True

# 	def make_active(modeladmin, request, queryset):
# 		queryset.update(is_active = 1)
# 		messages.success(request, "Selected Record(s) Marked as Active Successfully !!")

# 	def make_inactive(modeladmin, request, queryset):
# 		queryset.update(is_active = 0)
# 		messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")

# 	admin.site.add_action(make_active, "Make Active")
# 	admin.site.add_action(make_inactive, "Make Inactive")

# 	def has_delete_permission(self, request, obj = None):
# 		return False

# admin.site.register(State, StateAdmin)

#  Remove Add option
# from django.contrib import admin
# from .models import State

# class StateAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'active', 'created_on')

# 	def active(self, obj):
# 		return obj.is_active == 1

# 	active.boolean = True

# 	def has_add_permission(self, request):
# 		return False

# admin.site.register(State, StateAdmin)
