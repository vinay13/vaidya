from rest_framework import serializers
from survey.models import Survey,Question,Choice
from category.serializers import CategorySerializer


class ChoiceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Choice
		fields = ('choice','vote')


class QuestionSerializer(serializers.ModelSerializer):

	#choices = serializers.StringRelatedField(many=True)
	#choice=ChoiceSerializer(many=True)

	class Meta:
		model = Question
		fields = ('id','category','survey','question_type','choices','required')

#next do appreciation

class SurveySerializer(serializers.ModelSerializer):

	#questions = QuestionSerializer(many=True)
	#category = CategorySerializer() 
	#choices = serializers.StringRelatedField(many=True)
	
	class Meta:
		model = Survey
		fields=('id','title','user','created_at','updated_at')





