from django.db import models
from django.contrib.auth.models import User
 
class Task(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length=100)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['created']
		
	def __str__(self):
		return self.title
	
