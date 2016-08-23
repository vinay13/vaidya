from django.contrib import admin
from complaints.models import Complaint
# Register your models here.




@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
	list_display = ('id','title','body','category_id','against_id','anonymous','closedDate','assignedTo')



