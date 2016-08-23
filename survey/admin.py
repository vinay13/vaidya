from django.contrib import admin
from survey.models import Survey,Question,Choice

# Register your models here.


#@admin.register(Question)
class QuestionInline(admin.TabularInline):
	model  = Question
	list_display = ('id','required','category','survey','question_type','choices')




@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
	#list_display = ('id','title')
	inlines = [QuestionInline]


"""
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
	list_display = ('id','questionId','choice','vote')"""