from django.shortcuts import render
from rest_framework import viewsets
from category.models import Category , SubCategory
from category.serializers import CategorySerializer , SubCategorySerializer
from rest_framework import filters
# Create your views here.



class CategoryViewSet(viewsets.ModelViewSet):

	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):

	queryset = SubCategory.objects.all()
	serializer_class = SubCategorySerializer

