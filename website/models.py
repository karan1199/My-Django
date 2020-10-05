from django.db import models

# Create your models here.

class Project(models.Model):
	"""docstring for Project"""

	title = models.CharField(max_length=20)
	desc = models.CharField(max_length=120)
	img = models.ImageField(upload_to='')
	link =  models.URLField(max_length=200)
	
	def __str__(self):
		return self.title