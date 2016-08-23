from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from category.models import Category
# Create your models here.



class Appreciate(models.Model):

	id = models.AutoField(primary_key=True)
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	user = models.ForeignKey(User)
	text = models.TextField()
	created_at=models.DateTimeField(default=datetime.now)


	def __str__(self):
		return self.text


