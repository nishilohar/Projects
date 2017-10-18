from django.db import models

# Create your models here.
class QuestionAndAnswer(models.Model):
	question = models.CharField(max_length = 100)
	answer = models.TextField()
	askedBy = models.CharField(max_length = 50, default = "Anonymous")
	category = models.CharField(max_length = 20, null = True)
	updated = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.question