from rest_framework import serializers
from appreciations.models import Appreciate





class AppreciationSerializer(serializers.ModelSerializer):


	class Meta:

		model =Appreciate
		fields = '__all__'








