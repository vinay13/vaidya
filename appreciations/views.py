from django.shortcuts import render
from appreciations.models import Appreciate
from appreciations.serializers import AppreciationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.





class AppreciationList(APIView):


	def get(self,request,format=None):
		appre2=Appreciate.objects.all()
		serializer=AppreciationSerializer(appre2,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer=AppreciationSerializer(data = request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




