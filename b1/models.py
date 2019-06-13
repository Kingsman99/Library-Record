from django.db import models

# Create your models here.
class books(models.Model):

	bname=models.CharField(max_length=100)
	bauthor=models.CharField(max_length=150)
	bquan=models.CharField(max_length=500)
	