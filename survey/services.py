class Question(models.Model):
	TEXT = 'text'
	RADIO = 'radio'
	SELECT = 'select'
	SELECT_MULTIPLE = 'select-multiple'
	INTEGER = 'integer'

	QUESTION_TYPES = (
		(TEXT, 'text'),
		(RADIO, 'radio'),
		(SELECT, 'select'),
		(SELECT_MULTIPLE, 'Select Multiple'),
		(INTEGER, 'integer'),
	)

	text = models.TextField()
	required = models.BooleanField()
	category = models.ForeignKey(Category, blank=True, null=True,) 
	survey = models.ForeignKey(Survey)
	question_type = models.CharField(max_length=200, choices=QUESTION_TYPES, default=TEXT)
	# the choices field is only used if the question type 
	choices = models.TextField(blank=True, null=True,
		help_text='if the question type is "radio," "select," or "select multiple" provide a comma-separated list of options for this question .')

	def save(self, *args, **kwargs):
		if (self.question_type == Question.RADIO or self.question_type == Question.SELECT 
			or self.question_type == Question.SELECT_MULTIPLE):
			validate_list(self.choices)
		super(Question, self).save(*args, **kwargs)

	def get_choices(self):
		''' parse the choices field and return a tuple formatted appropriately
		for the 'choices' argument of a form widget.'''
		choices = self.choices.split(',')
		choices_list = []
		for c in choices:
			c = c.strip()
			choices_list.append((c,c))
		choices_tuple = tuple(choices_list)
		return choices_tuple

	def __str__(self):
		return (self.text)