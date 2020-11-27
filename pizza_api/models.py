from django.db import models

class shape_piza(models.Model):
	share = models.CharField(max_length=20)
	"""docstring for ClassName"""
class size_piza(models.Model):
	size = models.CharField(max_length=20)

class choice(models.Model):
	choice = models.CharField(max_length=20)	

class piza_type(models.Model):
	shape_id = models.ForeignKey(shape_piza, on_delete = models.CASCADE)
	size_id = models.ForeignKey(size_piza, on_delete = models.CASCADE)
	#choice = models.ForeignKey(choice, on_delete = models.CASCADE)
	choice = models.ManyToManyField(choice)

