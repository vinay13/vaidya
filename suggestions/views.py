from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from suggestions.models import Suggestion
from suggestions.serializers import SuggestionSerializers
# Create your views here.


@api_view(['GET', 'POST'])
def suggestion_list(request):

    if request.method == 'GET':
        polls = Suggestion.objects.all()
        serializer = SuggestionSerializers(polls, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuggestionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)