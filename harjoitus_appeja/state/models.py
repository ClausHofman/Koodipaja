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


# How to create Abstract Model Class in Django?

class common(models.Model):  # COMM0N
    abs_name = models.CharField(max_length=100)
  
    class Meta:
        abstract = True

class Student(common): # STUDENT
	rollno = models.IntegerField()
	def __str__(self):
		return self.abs_name

class Teacher(common): # TEACHER
	teacher_id = models.IntegerField()
	def __str__(self):
		return self.abs_name
# So have you notice that one field name is common on  both models.

# So instead of adding common fields in both models ,we have create a another model and put those 
# common fields in that model.
