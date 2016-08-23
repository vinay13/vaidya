from django.contrib import admin
from suggestions.models import Suggestion
# Register your models here.



@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):

	list_display = ('id','title','body','category_id','against_id','anonymous','createdDate','closedDate','user','assignedTo','priority')
