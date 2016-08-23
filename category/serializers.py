from rest_framework import serializers
from category.models import Category,SubCategory




class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields=('id','name')




class SubCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = SubCategory
		fields = ('id','category','name')