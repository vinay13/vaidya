from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from complaints.models import Complaint
from complaints.serializers import ComplaintSerializer
from complaints.email import sendEmail
from django.core.mail import send_mail



class ComplaintList(APIView):

	def get(self,request,format=None):
		complaints = Complaint.objects.all()
		serializer = ComplaintSerializer(complaints, many=True)
		return Response(serializer.data)


	def post(self,request,format=None):
		serializer = ComplaintSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			sendEmail()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ComplaintDetail(APIView):

	def get_object(self, pk):
		try:
			return Complaint.objects.get(pk=pk)
		except Complaint.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		complaints2 = self.get_object(pk)
		serializer = ComplaintSerializer(complaints2)
		return Response(serializer.data)