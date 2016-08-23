from django.contrib import admin
from category.models import Category,SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	#fields  = ('id','title','body','event_date','start_time','end_time','event_type_id','event_standard')
	list_display = ('id','name')



@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
	list_display = ('id','category','name')