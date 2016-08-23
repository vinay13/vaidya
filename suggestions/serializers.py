from rest_framework import serializers
from suggestions.models import Suggestion




class SuggestionSerializers(serializers.ModelSerializer):
	Model = Suggestion
	fields ='__all__'
