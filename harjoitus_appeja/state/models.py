from django.db import models
from django.utils import timezone

class State(models.Model):
	name = models.CharField(max_length = 50)
	is_active = models.IntegerField(default = 1,
								blank = True,
									null = True,
									help_text ='1->Active, 0->Inactive',
									choices =(
									(1, 'Active'), (0, 'Inactive')
									))
	created_on = models.DateTimeField(default = timezone.now)
	updated_on = models.DateTimeField(default = timezone.now,
									null = True,
									blank = True
									)
	def __str__(self):
		return self.name
	class Meta:
		db_table = 'state'
		# Add verbose name
		verbose_name = 'State List'
