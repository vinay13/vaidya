from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from category.models import Category
from django.core.exceptions import ValidationError


class Survey(models.Model):
	id = models.AutoField(primary_key=True)
	title=models.CharField(max_length=128,blank=True)
	description = models.TextField(blank=True)
	#category = models.ForeignKey(Category,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	created_at = models.DateTimeField(default = datetime.now)
	updated_at = models.DateTimeField(default = datetime.now)

	def __str__(self):
		return self.title 



def validate_list(value):
	values = value.split(',')
	if len(values) < 2 :
		raise ValidationError("The selected field requires an associated list of choices.")





class Question(models.Model):
	TEXT = 'text'
	RADIO = 'radio'
	SELECT = 'select'
	SELECT_MULTIPLE = 'select-multiple'
	INTEGER = 'integer'

	QUESTION_TYPES = (
		(TEXT, 'text'),
		(RADIO, 'radio'),
		(SELECT, 'select'),
		(SELECT_MULTIPLE, 'Select Multiple'),
		(INTEGER, 'integer'),
	)

	text = models.TextField()
	required = models.BooleanField(default=True)
	category = models.ForeignKey(Category, blank=True, null=True,) 
	survey = models.ForeignKey(Survey,on_delete = models.CASCADE)
	question_type = models.CharField(max_length=200, choices=QUESTION_TYPES, default=TEXT)
	# the choices field is only used if the question type 
	choices = models.TextField(blank=True, null=True,
		help_text='if the question type is "radio," "select," or "select multiple" provide a comma-separated list of options for this question .')

	def save(self, *args, **kwargs):
		if (self.question_type == Question.RADIO or self.question_type == Question.SELECT 
			or self.question_type == Question.SELECT_MULTIPLE):
			validate_list(self.choices)
		super(Question, self).save(*args, **kwargs)

	def get_choices(self):
		''' parse the choices field and return a tuple formatted appropriately
		for the 'choices' argument of a form widget.'''
		choices = self.choices.split(',')
		choices_list = []
		for c in choices:
			c = c.strip()
			choices_list.append((c,c))
		choices_tuple = tuple(choices_list)
		return choices_tuple

	def __str__(self):
		return (self.text)



class Choice(models.Model):
	id = models.AutoField(primary_key=True)
	questionId = models.ForeignKey(Question,related_name='choice',on_delete = models.CASCADE)
	choice = models.CharField(max_length=123,blank=True)
	vote = models.IntegerField(null=True,default=0)

	def __str__(self):
		return self.choice




class Response(models.Model):

	id = models.AutoField(primary_key=True)
 	created_at = models.DateTimeField(default = datetime.now)
	survey = models.ForeignKey(Survey)
	survey_user = models.CharField('Name of the user',max_length=233)
	comments = models.CharField(max_length=233,blank=True)


	def __str__(self):
		return self.survey_user




class Answer(models.Model):
	id = models.AutoField(primary_key=True)
	question = models.ForeignKey(Question)
	response = models.ForeignKey(Response)
	count = models.CharField(max_length=6,blank=True)


	def __str__(self):
		return self.response



	