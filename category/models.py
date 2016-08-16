from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length=123,blank=True)


	def __str__(self):
		return self.name