from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from allauth.account.signals import user_logged_in, user_signed_up

# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length=120)
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	bio = models.TextField(default='bio default text')
	address = models.CharField(max_length=100, null=True, blank=True)
	birth_date = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return self.name
