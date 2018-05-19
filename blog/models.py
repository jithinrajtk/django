from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.date = timezone.now
		self.save()
		
	def __str__(self):
		return self.title
		pass


# Create your models here.
