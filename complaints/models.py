from django.db import models
from django.contrib.auth.models import User,Group
from category.models import Category
# Create your models here.
from base.constants import ComplaintStatus



class Complaint(models.Model):

	id = models.AutoField(primary_key = True)
	title = models.CharField(max_length=233,blank=True)
	body = models.TextField()
	category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
	against_id = models.ForeignKey(User,related_name = 'Against',on_delete=models.CASCADE)
	anonymous = models.BooleanField(default = False)
	closedDate = models.DateField(null=True,blank=True)
	assignedTo = models.ForeignKey(User,related_name = 'AssignedTo' ,on_delete=models.CASCADE)
	status = models.PositiveSmallIntegerField(choices = ComplaintStatus.CHOICES,
											default = ComplaintStatus.OPEN)
	
	def __str__(self):
		return self.title
