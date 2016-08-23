from django.shortcuts import render
from survey.models import Survey,Question
from survey.serializers import SurveySerializer,QuestionSerializer,ChoiceSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import json


class SurveyView(APIView):

	def get(self,request,format=None):
		surveys=Survey.objects.all()
		serializer=SurveySerializer(surveys,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer=SurveySerializer(data = request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class SurveyDetail(APIView):

	def get_object(self, pk):
		try:
			return Survey.objects.get(pk=pk)
		except Survey.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		survey3 = self.get_object(pk)
		serializer = SurveySerializer(survey3)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		survey3= self.get_object(pk)
		serializer = SurveySerializer(survey3, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		survey3 = self.get_object(pk)
		survey3.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)






class QuestionView(APIView):

	def get(self,request,format=None):
		#get_choices
		questions = Question.objects.all()
		serializer = QuestionSerializer(questions,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = QuestionSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class QuestionDetail(APIView):

	def get_object(self,pk):
		try:
			return Question.objects.get(pk=pk)
		except Question.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		quest4 = self.get_object(pk)
		serializer = QuestionSerializer(quest4)
		return Response(serializer.data)


	def put(self,request,pk,format=None):
		quest4= self.get_object(pk)
		serializer = QuestionSerializer(quest4, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request, pk, format=None):
		quest4 = self.get_object(pk)
		quest4.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)




"""
class GetChoices(APIView):

	def get(self,request,format=None):
		getchoices5=Question()
		serializer = getchoices5.get_choices()
		return Response(serializer.data)
"""



class ChoiceView(APIView):

	def get(self,request,format=None):
		choices = Choice.objects.all()
		serializer= ChoiceSerializer(choices,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = ChoiceSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class ChoiceDetail(APIView):

	def get_object(self,pk):
		try:
			return Choice.objects.get(pk=pk)
		except Choice.DoesNotExist:
			raise Http404

	def delete(self,request,pk,format=None):
		choice3 = self.get_object(pk)
		survey3.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


