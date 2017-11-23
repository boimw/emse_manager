from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=300)

class Idea(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=300)
	catId = models.ForeignKey(Category, on_delete=models.CASCADE)
	owner=models.ForeignKey(User,on_delete=models.CASCADE)

class Comment(models.Model):
    	comment = models.CharField(max_length=50)
	likeCount = models.IntegerField(default=0)
	date = models.DateTimeField(auto_now_add=True)
	idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	

class Rating(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE)
	ideaId = models.ForeignKey(Idea, on_delete=models.CASCADE)
	rating = models.IntegerField(default=5)
