from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Idea(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=300)
	owner=models.ForeignKey(User,on_delete=models.CASCADE)

class Rating(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE)
	ideaId = models.ForeignKey(Idea, on_delete=models.CASCADE)
	rating = models.IntegerField(default=5)
