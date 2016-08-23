class Question(models.Model):

	id = models.AutoField(primary_key=True)
	surveyId = models.ForeignKey(Survey,related_name='questions',on_delete=models.CASCADE)
	question = models.CharField(max_length=255,blank=True)

	def __str__(self):
		return self.question 
